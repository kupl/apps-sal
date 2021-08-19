(N, K) = map(int, input().split())
A = list(map(int, input().split()))


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)
A.sort()
(max_sum, min_sum) = (0, 0)
for i in range(N - 1, K - 2, -1):
    max_i = A[i]
    max_sum += A[i] * cmb(i, K - 1, p) % p
    max_sum %= p
    j = N - 1 - i
    min_j = A[j]
    min_sum += A[j] * cmb(i, K - 1, p) % p
    min_sum %= p
ans = (max_sum - min_sum) % p
print(ans)
