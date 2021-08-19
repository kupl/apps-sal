def power(a, pow1, MOD):
    if pow1 == 0:
        return 1
    elif pow1 % 2 == 1:
        return power(a, pow1 - 1, MOD) * a % MOD
    else:
        return power(a, pow1 // 2, MOD) ** 2 % MOD


n = int(input())
MOD = 10
print(power(1378, n, MOD))
