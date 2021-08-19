import sys
(N, K) = map(int, sys.stdin.readline().split())
ans = 0
for i in range(1, N + 1):
    if K <= i:
        ans += 1 / N
    else:
        count = 0
        while i < K:
            count += 1
            i *= 2
        ans += 1 / N * 0.5 ** count
print(ans)
