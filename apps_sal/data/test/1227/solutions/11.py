N = input()
k = int(input())
# 桁数
length = len(N)
# dp[ 決めた桁数 ][ 未満フラグ ][0以外の個数] := 総数
dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(length + 1)]
dp[0][0][0] = 1

for i in range(length):
    max_digit = int(N[i])

    for k_num in range(k + 1):
        for flag_less in range(2):
            range_digit = 9 if flag_less else max_digit
            for d in range(range_digit + 1):
                flag_less_next = 0
                if flag_less == 1 or d < max_digit:
                    flag_less_next = 1
                # 0 の時は0以外の個数は増えない
                k_num_next = k_num
                if d != 0:
                    k_num_next = k_num + 1
                    if k_num_next > k:
                        continue
                dp[i + 1][flag_less_next][k_num_next] += dp[i][flag_less][k_num]
print((dp[length][0][k] + dp[length][1][k]))
