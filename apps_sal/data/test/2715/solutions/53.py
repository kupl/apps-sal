import sys

K = int(sys.stdin.readline())

N = 50
V = [49 + K // 50 for _ in range(N)]

K %= 50
for i in range(K):
    V[i] += N+1
    for j in range(N):
        V[j] -= 1

print(N)
print(*V)
