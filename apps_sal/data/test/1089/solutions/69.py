# inverse x^(-1)
def inv(x):
    nonlocal mod
    return pow(x, mod - 2, mod)

# factorial x!
def fact(x):
    nonlocal mod
    res=1
    for i in range(2 , x + 1):
        res=res * i % mod
    return res

# combination nCr
def combi(n,r):
    if r < 0 or r > n:
        return 0
    else:
        return fact(n) * inv(fact(r)) * inv(fact(n - r)) % mod

mod = 10 ** 9 + 7
N, M, K = map(int,input().split())
x = (N - 1) * N * (N + 1) * inv(6) % mod
x = x * M * M % mod
y = (M - 1) * M * (M + 1) * inv(6) % mod
y = y * N * N % mod
z = combi(M * N - 2, K - 2)
ans = (x + y) * z % mod
print(ans)
