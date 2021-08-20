n = int(input())


def dfs(s):
    if int(s) > n:
        return 0
    cnt = 0
    if all((i in s for i in '357')):
        cnt = 1
    for i in '357':
        cnt += dfs(s + i)
    return cnt


print(dfs('0'))
