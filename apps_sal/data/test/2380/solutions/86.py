from bisect import bisect_left

N, M = map(int, input().split())
d = dict()
A = list(map(int, input().split()))
for i in range(N):
    d[A[i]] = d.get(A[i], 0) + 1
for i in range(M):
    B, C = map(int, input().split())
    d[C] = d.get(C, 0) + B

ans = 0
keys = sorted(list(d.keys()), reverse=True)
for k in keys:
    kosuu = min(N, d.get(k))
    ans += k * kosuu
    N -= kosuu
    if N == 0:
        break
print(ans)
