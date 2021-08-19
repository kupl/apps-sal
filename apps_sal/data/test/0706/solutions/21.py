(a, b, n, x) = map(int, input().split())
MOD = 1000000007
cur = x
while n > 0:
    if n & 1:
        cur = (a * cur + b) % MOD
    (a, b) = (a * a % MOD, (a * b + b) % MOD)
    n >>= 1
print(cur)
