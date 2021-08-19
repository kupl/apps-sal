N, K = [int(s) for s in input().split()]
P = [int(s) for s in input().split()]

# Piの期待値 (1 + Pi) // 2
E = list(map(lambda x: (x + 1) / 2, P))
E_SUMS = [E[0]]
for i in range(1, N):
    E_SUMS.append(E_SUMS[i - 1] + E[i])

m = E_SUMS[K - 1]
for i in range(K, N):
    m = max(m, E_SUMS[i] - E_SUMS[i - K])

print(m)
