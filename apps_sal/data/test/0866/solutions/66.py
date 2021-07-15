# 73

MOD = 10**9 + 7
x, y = list(map(int, input().split()))

a = 2*y - x
b = 2*x - y

fac_l = [0] * (int((a + b) / 3) + 1)
inv_l = [0] * (int((a + b) / 3) + 1)
finv_l = [0] * (int((a + b) / 3) + 1)


def com_init():
    fac_l[1] = 1
    inv_l[0] = 1
    inv_l[1] = 1
    finv_l[0] = 1
    finv_l[1] = 1
    for i in range(2, a+b+1):
        fac_l[i] = (fac_l[i-1] * i) % MOD
        inv_l[i] = MOD - (inv_l[MOD % i] * int(MOD / i)) % MOD
        finv_l[i] = (finv_l[i-1] * inv_l[i]) % MOD

def ncr(n, r):
    return (fac_l[n] * (finv_l[r] * finv_l[n-r]) % MOD) % MOD


if a % 3 != 0 or b % 3 != 0 or a < 0 or b < 0:
    print("0")
else:
    a = int(a/3)
    b = int(b/3)

    com_init()
    print((ncr(a+b, a)))

