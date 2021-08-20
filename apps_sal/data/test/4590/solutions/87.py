import bisect
(N, M, K) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = [0]
for i in range(N):
    a.append(a[i] + A[i])
ak = [i - K for i in a]
b = [0]
for i in range(M):
    b.append(b[i] - B[i])
ans = 0
for i in range(M + 1):
    k = bisect.bisect_right(ak, b[i])
    if k > 0:
        ans = max(k + i - 1, ans)
print(ans)
