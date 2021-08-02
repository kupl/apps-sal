import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
mx = max(a)
mn = min(a)
res = []
if abs(mx) >= abs(mn):
    t = 0
    for i in range(N):
        if a[i] == mx:
            t = i
            break
    for i in range(N):
        res.append((t + 1, i + 1))
        a[i] += a[t]
    for i in range(N):
        for j in range(N):
            if a[j] > a[t]: t = j
        res.append((t + 1, i + 1))
        a[i] += a[t]
    print(len(res))
    for r in res: print(*r)
else:
    t = 0
    for i in range(N):
        if a[i] == mn:
            t = i
            break
    for i in range(N):
        res.append((t + 1, i + 1))
        a[i] += a[t]
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if a[j] < a[t]: t = j
        res.append((t + 1, i + 1))
        a[i] += a[t]
    print(len(res))
    for r in res: print(*r)
