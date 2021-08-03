from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**6)
n, k = map(int, input().split())
paths = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    paths[a - 1].append(b - 1)
    paths[b - 1].append(a - 1)
inf = 100000000000000
nums = [-inf] * n
nums[0] = k
now = deque()
now.append(0)


def bfs(d):
    nonlocal n, k, paths, nums, now
    l = len(now)
    if d == 1:
        for i in range(l):
            p = now.popleft()
            ln = len(paths[p])
            next_num = k - 1
            for j in range(ln):
                if nums[paths[p][j]] == -inf:
                    nums[paths[p][j]] = next_num
                    now.append(paths[p][j])
                    next_num -= 1
    else:
        for i in range(l):
            p = now.popleft()
            ln = len(paths[p])
            next_num = k - 2
            for j in range(ln):
                if nums[paths[p][j]] == -inf:
                    nums[paths[p][j]] = next_num
                    now.append(paths[p][j])
                    next_num -= 1
    if len(now):
        bfs(d + 1)


bfs(1)
ans = 1
for i in range(n):
    if nums[i] <= 0:
        print(0)
        return
    ans *= nums[i]
    ans %= (10**9 + 7)
print(ans)
