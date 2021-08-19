N = int(input())
T = ('3', '5', '7')


def dfs(x):
    if x != '' and int(x) > N:
        return 0
    res = 0
    if len(set(x)) == 3:
        res = 1
    for t in T:
        res += dfs(x + t)
    return res


print(dfs(''))
