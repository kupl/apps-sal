from bisect import bisect_left
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
cums = [0]
for a in A:
    cums.append(cums[-1] + a)
ans = 0
for i in range(N):
    j = bisect_left(cums, cums[i] + K)
    ans += N + 1 - j
print(ans)
