import bisect
(N, K) = map(int, input().split())
A = [int(i) for i in input().split()]
ans = 0
'\nr = 0\nl = 0\ns = 0\nfor r in range(N) :\n    s += A[r]\n    while s >= K : \n        ans += N-r\n        s -= A[l]\n        l += 1\n        \nprint(ans)\n'
cusum = [0]
for i in range(N):
    cusum.append(cusum[i] + A[i])
for i in cusum:
    if i < K:
        continue
    ans += bisect.bisect(cusum, i - K)
print(ans)
