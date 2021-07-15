n, m = list(map(int, input().split()))
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

MOD = 10 ** 9 + 7
invm = pow(m, MOD - 2, MOD)
inv2 = pow(2, MOD - 2, MOD)

z = 0
p = 1

for a, b in zip(s1, s2):
    if a == 0 and b == 0:
        z = (z + p * ((m - 1) * (invm * inv2))) % MOD
        p = (p * invm) % MOD
    elif a == 0:
        z = (z + (p * (m - b) * invm)) % MOD
        p = (p * invm) % MOD
    elif b == 0:
        z = (z + (p * (a - 1) * invm)) % MOD
        p = (p * invm) % MOD
    elif a > b:
        z = (z + p) % MOD
        break
    elif a < b:
        break
print(z)

