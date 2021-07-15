fact = [1]


def c_n_k(k, n):
    return fact[n] // (fact[k] * fact[n - k])

n, k = map(int, input().split())

for i in range(1, n + 1):
    fact.append(i * fact[i - 1])

ans = 1

d = [0, 0, 1, 3, 12, 60, 124]

for i in range(k, 1, -1):
    ans += c_n_k(i, n) * (d[i] - d[i] // i)

print(ans)
