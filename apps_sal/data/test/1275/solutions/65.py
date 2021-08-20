import sys
(N, K) = map(int, input().split())
cnt = 0
for q in range(max(2 - K, 2), min(2 * N - K + 1, 2 * N + 1)):
    p = K + q
    if p - 1 > N and q - 1 > N:
        cnt = cnt + (abs(2 * N - p) + 1) * (abs(2 * N - q) + 1)
    elif q - 1 > N:
        cnt = cnt + (abs(2 * N - q) + 1) * (p - 1)
    elif p - 1 > N:
        cnt = cnt + (abs(2 * N - p) + 1) * (q - 1)
    else:
        cnt = cnt + (q - 1) * (p - 1)
print(cnt)
