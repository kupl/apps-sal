n, k = map(int, input().split())
C = [0] + list(map(int, input().split()))
K = set(map(int, input().split()))

F = [0] * (n + 1)
G = [0] * (n + 2)

for i in range(1, n + 1):
    F[i] = F[i - 1] + C[i]
    if i in K:
        G[i] = G[i - 1]
    else:
        G[i] = G[i - 1] + C[i]


summa = 0
for i in range(1, n + 1):
    if i in K:
        summa += G[i - 2] * C[i]
        summa += (F[n] - F[i]) * C[i]

    elif i < n:
        summa += C[i] * C[i + 1]

    elif i == n and 1 not in K:
        summa += C[1] * C[i]


print(summa)
