def get_next_unchosen(current, chooseNum):
    if (chooseNum, 0) in current or (chooseNum, 1) in current:
        if (chooseNum, 0) in current and (chooseNum, 1) in current:
            return max(current[(chooseNum, 0)], current[(chooseNum, 1)])
        if (chooseNum, 0) in current:
            return current[(chooseNum, 0)]
        return current[(chooseNum, 1)]
    return None


def calc_next_state(current, must_choose_num, a):
    next = {}
    current_unchosen_nums = [choose_num for (choose_num, prev_chosen) in list(current.keys()) if prev_chosen == 0 and choose_num >= must_choose_num - 1]
    for chooseNum in current_unchosen_nums:
        next[(chooseNum + 1, 1)] = current[(chooseNum, 0)] + a
    for chooseNum in range(must_choose_num, N):
        n = get_next_unchosen(current, chooseNum)
        if n is None:
            break
        else:
            next[(chooseNum, 0)] = n
    return next


N = int(input())
A = [int(x) for x in input().split()]

totalChooseNum = N // 2
dp = {(0, 0): 0}
for i in range(0, N):
    ai = A[i]
    canChooseNum = (N - i + 1) // 2
    mustChooseNum = max(totalChooseNum - canChooseNum, 0)
    dp = calc_next_state(dp, mustChooseNum, ai)

result = max(dp[(totalChooseNum, 0)], dp[(totalChooseNum, 1)])
print(result)
