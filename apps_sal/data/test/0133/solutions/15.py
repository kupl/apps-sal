(n, m) = [int(x) for x in input().split()]
mod = int(1000000000.0) + 7
n1 = (pow(2, m, mod) - 1 + mod) % mod
n1 = pow(n1, n, mod)
print(n1)
