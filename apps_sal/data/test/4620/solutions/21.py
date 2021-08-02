N = int(input())
C, S, F = map(list, zip(*[list(map(int, input().split())) for i in range(N - 1)]))
r = [0] * N
for i in range(N - 2, -1, -1):
    x = S[i] + C[i]
    for j in range(i + 1, N - 1):
        x = S[j] + C[j] if x < S[j] else -(-x // F[j]) * F[j] + C[j]
    r[i] = x
print(*r, sep='\n')
