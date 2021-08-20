import sys
readline = sys.stdin.readline
(N, K) = map(int, readline().split())
A = list((int(x) for x in readline().split()))
bits = [0] * 50
for i in range(N):
    for j in range(50):
        if A[i] >> j & 1:
            bits[j] += 1
ans = 0
tmp_K = 0
tmp_greed = 0
for i in range(50)[::-1]:
    if K >> i & 1:
        tmp_greed = bits[i] * 1 << i
        for j in range(i)[::-1]:
            tmp_greed += max(bits[j], N - bits[j]) * 1 << j
        ans = max(tmp_greed + tmp_K, ans)
        tmp_K += (N - bits[i]) * 1 << i
    else:
        tmp_K += bits[i] * 1 << i
ans = max(ans, tmp_K)
print(ans)
