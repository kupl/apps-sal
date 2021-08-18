import sys
N, M = map(int, input().split())
if not (1 <= N <= 10**12 and 1 <= M <= 10**12):
    return

count_SCC = 0
if M > 2 * N:  # Mがあまる
    M = M - 2 * N
    count_SCC = N + M // 4
elif M < 2 * N:  # Nがあまる
    count_SCC = M // 2
print(count_SCC)
