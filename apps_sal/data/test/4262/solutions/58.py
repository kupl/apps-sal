import itertools


def count_order():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    permutations_list = itertools.permutations((x for x in range(1, N + 1)))
    count = 0
    for one_case in permutations_list:
        count += 1
        for i in range(len(one_case)):
            if one_case[i] == P[i]:
                is_ok_P = True
            else:
                is_ok_P = False
                break
        if is_ok_P:
            a = count
        for i in range(len(one_case)):
            if one_case[i] == Q[i]:
                is_ok_Q = True
            else:
                is_ok_Q = False
                break
        if is_ok_Q:
            b = count
    return abs(a - b)


result = count_order()
print(result)
