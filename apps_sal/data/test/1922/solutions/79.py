import sys

N, M = map(int, input().split())

if N == 1 and 3 <= M:
    print(M - 2)
    return
if M == 1 and 3 <= N:
    print(N - 2)
    return
print(M * N - (2 * N + 2 * M - 4))
