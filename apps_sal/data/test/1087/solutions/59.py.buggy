
N, K = list(map(int, input().split()))
A_list = list(map(int, input().split()))

max_a = max(max(A_list), K)
max_len = 0
tmp = max_a
while tmp > 0:
    max_len += 1
    tmp //= 2

K_bits = [1 if (K >> j & 1) else 0 for j in range(max_len)][::-1]

sum_1_bits = [0] * max_len
for a in A_list:
    a_bits = [j for j in range(max_len) if (a >> j & 1)]
    for bit in a_bits:
        sum_1_bits[bit] += 1
sum_1_bits = sum_1_bits[::-1]

# dp start
# dp[is未満][桁]
dp = [[0] * max_len for i in range(2)]
border = N / 2
twice = 2 ** (max_len - 1)
highest_digit = 0
i = 0

if K == 0:
    res = 0
    for b in sum_1_bits:
        res += twice * b
        twice //= 2

    print(res)
    return

while True:
    if K_bits[i] == 1:
        highest_digit = i
        break
    dp[0][i] = dp[0][i - 1] + twice * sum_1_bits[i]
    dp[1][i] = dp[1][i - 1] + twice * sum_1_bits[i]
    twice //= 2
    i += 1

dp[0][highest_digit] = dp[0][highest_digit - 1] + twice * (N - sum_1_bits[highest_digit])
dp[1][highest_digit] = dp[1][highest_digit - 1] + twice * sum_1_bits[highest_digit]
twice //= 2

for i in range(highest_digit + 1, max_len):

    ibits = sum_1_bits[i]
    dp[1][i] = dp[1][i - 1] + twice * max(ibits, N - ibits)
    if K_bits[i] == 1:
        dp[1][i] = max(dp[1][i], dp[0][i - 1] + twice * ibits)
    k_side = ibits if K_bits[i] == 0 else N - ibits
    dp[0][i] = dp[0][i - 1] + twice * k_side
    twice //= 2

print((max(dp[0][-1], dp[1][-1])))
