from bisect import *
n,k = list(map(int,input().split()))
A = list(map(int,input().split()))

s = 0
sl = {0:[0]}
for i in range(n):
    s += A[i] - 1
    s %= k
    if s not in list(sl.keys()):
        sl[s] = []
    sl[s].append(i+1)
ans = 0
for ls in list(sl.values()):
    for i,l in enumerate(ls):
        x = bisect_right(ls, l + k - 1)
        ans += x - i - 1
print(ans)

