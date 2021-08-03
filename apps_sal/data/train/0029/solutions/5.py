import sys
sys.setrecursionlimit(1000000)

T = int(input())
for _ in range(T):
    n = int(input())
    a = [int(x) - 1 for x in input().split()]
    prev = [-1 for _ in range(n)]
    val = [1 for _ in range(n)]
    for i, x in enumerate(a):
        delta = i - prev[x]
        val[x] = max(val[x], delta)
        prev[x] = i
    for i in range(n):
        val[i] = max(val[i], n - prev[i])
    ans = [-1 for _ in range(n + 1)]
    r = n + 1
    for i in range(n):
        if val[i] < r:
            for j in range(val[i], r):
                ans[j] = i + 1
            r = val[i]
    print(' '.join([str(x) for x in ans[1:]]))
