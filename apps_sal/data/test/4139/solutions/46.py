n = int(input())


def dfs(x):
    if x != '' and n < int(x):
        return 0
    if set(x) == {'3', '5', '7'}:
        c = 1
    else:
        c = 0
    for i in '357':
        c += dfs(x + i)
    return c


print(dfs(''))
