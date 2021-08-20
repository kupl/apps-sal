(n, l, r) = [int(i) for i in input().split()]
number_of_zeros = 0
number_of_ones = 0
number_of_twos = 0
if l % 3 == 0:
    if r % 3 == 0:
        number_of_zeros = (r - l + 1) // 3 + 1
        number_of_ones = (r - l + 1) // 3
        number_of_twos = (r - l + 1) // 3
    if r % 3 == 1:
        number_of_zeros = (r - l + 1) // 3 + 1
        number_of_ones = (r - l + 1) // 3 + 1
        number_of_twos = (r - l + 1) // 3
    if r % 3 == 2:
        number_of_zeros = (r - l + 1) // 3
        number_of_ones = (r - l + 1) // 3
        number_of_twos = (r - l + 1) // 3
elif l % 3 == 1:
    if r % 3 == 0:
        number_of_zeros = (r - l + 1) // 3
        number_of_ones = (r - l + 1) // 3
        number_of_twos = (r - l + 1) // 3
    if r % 3 == 1:
        number_of_zeros = (r - l + 1) // 3
        number_of_ones = (r - l + 1) // 3 + 1
        number_of_twos = (r - l + 1) // 3
    if r % 3 == 2:
        number_of_zeros = (r - l + 1) // 3
        number_of_ones = (r - l + 1) // 3 + 1
        number_of_twos = (r - l + 1) // 3 + 1
elif l % 3 == 2:
    if r % 3 == 0:
        number_of_zeros = (r - l + 1) // 3 + 1
        number_of_ones = (r - l + 1) // 3
        number_of_twos = (r - l + 1) // 3 + 1
    if r % 3 == 1:
        number_of_zeros = (r - l + 1) // 3
        number_of_ones = (r - l + 1) // 3
        number_of_twos = (r - l + 1) // 3
    elif r % 3 == 2:
        number_of_zeros = (r - l + 1) // 3
        number_of_ones = (r - l + 1) // 3
        number_of_twos = (r - l + 1) // 3 + 1
dp = [[-1 for i in range(3)] for j in range(n + 1)]
MOD = 10 ** 9 + 7
dp[1][0] = number_of_zeros % MOD
dp[1][1] = number_of_ones % MOD
dp[1][2] = number_of_twos % MOD
for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] % MOD * (number_of_zeros % MOD) % MOD + dp[i - 1][1] % MOD * (number_of_twos % MOD) % MOD + dp[i - 1][2] % MOD * (number_of_ones % MOD) % MOD) % MOD
    dp[i][1] = (dp[i - 1][0] % MOD * (number_of_ones % MOD) % MOD + dp[i - 1][1] % MOD * (number_of_zeros % MOD) % MOD + dp[i - 1][2] % MOD * (number_of_twos % MOD) % MOD) % MOD
    dp[i][2] = (dp[i - 1][0] % MOD * (number_of_twos % MOD) % MOD + dp[i - 1][1] % MOD * (number_of_ones % MOD) % MOD + dp[i - 1][2] % MOD * number_of_zeros % MOD % MOD) % MOD
if dp[n][0] != -1:
    print(dp[n][0] % MOD)
else:
    print(0)
