from sys import setrecursionlimit
setrecursionlimit(10 ** 5)
k = int(input())


def dfs(d, val, alls):
    alls.append(val)
    if d == 10:
        return
    for i in range(-1, 2):
        a = val % 10 + i
        if a >= 0 and a <= 9:
            dfs(d + 1, val * 10 + a, alls)


alls = list()
for i in range(1, 10):
    dfs(1, i, alls)
alls.sort()
print(alls[k - 1])
