(n, m, k) = [int(t) for t in open(0).read().split()]
mod = 998244353
mem = [0] * max(k + 3, n + 1)
for i in range(k + 2):
    mem[i] = pow(m, i, mod)
c = 1
for i in range(k + 2, n + 1):
    mem[i] = (m * mem[i - 1] - m * c * pow(m - 1, i - k - 2, mod)) % mod
    c = c * (i - 1) * pow(i - k - 1, -1, mod) % mod
print(mem[n])
