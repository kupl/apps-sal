from sys import setrecursionlimit

a = int(input())

setrecursionlimit(200000)

h = [[] for i in range(a)]
s = list(map(int, input().split()))
for i in range(a - 1):
    h[s[i] - 1].append(i + 1)

metka = [False for i in range(a)]
dat = [0 for i in range(a)]
dis = [0 for i in range(a)]


def dfs(x):
    stack = []
    stack.append(x)
    while stack:
        x = stack.pop(-1)
        dat[dis[x]] += 1
        metka[x] = True
        for i in h[x]:
            if not metka[i]:
                stack.append(i)
                dis[i] = dis[x] + 1


dfs(0)

print(sum([x % 2 for x in dat]))

