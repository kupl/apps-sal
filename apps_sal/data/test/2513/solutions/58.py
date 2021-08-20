def add_ans(i, ans, circle):
    if circle[i] == 'o':
        if ans[i] == 'S':
            ans += ans[i - 1]
        elif ans[i - 1] == 'S':
            ans += 'W'
        else:
            ans += 'S'
    if circle[i] == 'x':
        if ans[i] == 'W':
            ans += ans[i - 1]
        elif ans[i - 1] == 'S':
            ans += 'W'
        else:
            ans += 'S'
    return ans


def check_last(ans, circle):
    if circle[0] == 'o':
        if ans[0] == 'S':
            last = ans[1]
        elif ans[1] == 'S':
            last = 'W'
        else:
            last = 'S'
    if circle[0] == 'x':
        if ans[0] == 'W':
            last = ans[1]
        elif ans[1] == 'S':
            last = 'W'
        else:
            last = 'S'
    if circle[-1] == 'o':
        if ans[-1] == 'S':
            first = ans[-2]
        elif ans[-2] == 'S':
            first = 'W'
        else:
            first = 'S'
    if circle[-1] == 'x':
        if ans[-1] == 'W':
            first = ans[-2]
        elif ans[-2] == 'S':
            first = 'W'
        else:
            first = 'S'
    if (last == ans[-1]) & (first == ans[0]):
        return 1
    else:
        return 0


flag = True
n = int(input())
circle = input()
ans_list = ['SS', 'SW', 'WS', 'WW']
for ans in ans_list:
    for i in range(1, len(circle) - 1):
        ans = add_ans(i, ans, circle)
    if check_last(ans, circle) == 1:
        print(ans)
        flag = False
        break
if flag:
    print('-1')
