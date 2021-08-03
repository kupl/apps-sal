from collections import deque
import sys
sys.setrecursionlimit(10**7)
n = int(input())
ad_ls = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    ad_ls[a - 1].append([b - 1, w])
    ad_ls[b - 1].append([a - 1, w])

cost_ls = [0] * n
done_ls = [0] * n


def dfs(v, c):
    for new, cost in ad_ls[v]:
        if not done_ls[new]:
            cost_ls[new] = c + cost
            done_ls[new] = 1
            dfs(new, c + cost)


dfs(0, 0)

color_ls = [0] * n
for i in range(n):
    color_ls[i] = cost_ls[i] % 2

for color in color_ls:
    print(color)
