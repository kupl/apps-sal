N, K = map(int, input().split())
D = [0] * (K + 1)
D[K] = 1
mod = 10**9 + 7
for i in range(K, 0, -1):
    D[i] = pow(K // i, N, mod)
    for j in range(2 * i, K + 1, i):
        D[i] = (D[i] - D[j]) % mod

c = 0
for i in range(len(D)):
    c += D[i] * i
print(c % mod)
