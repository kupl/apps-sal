import heapq


def dfs(x):
    if 0 < x <= n:
        s.add(x)
        x *= 10
        dfs(x + i)
        dfs(x + j)


n = int(input())
s = set()

for i in range(1, 10):
    for j in range(10):
        dfs(i)
print(len(s))
