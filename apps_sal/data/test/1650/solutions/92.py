MOD = 10**9 + 7

L = input()

dp1 = [0] * 100010  # dp1[k]: 先頭からk桁について，A+B < L が確定している (A,B) の数
dp2 = [0] * 100010  # dp2[k]: 先頭からk桁について，A+B と L が一致している (A,B) の数
dp1[1], dp2[1] = 1, 2

for i in range(1, len(L)):
    for digit_A, digit_B in [[0, 0], [0, 1], [1, 0]]:
        dp1[i + 1] += dp1[i]

        if digit_A + digit_B == int(L[i]):
            dp2[i + 1] += dp2[i]
        elif digit_A + digit_B < int(L[i]):
            dp1[i + 1] += dp2[i]

        dp1[i + 1] %= MOD
        dp2[i + 1] %= MOD

ans = dp1[len(L)] + dp2[len(L)]
print(ans % MOD)
