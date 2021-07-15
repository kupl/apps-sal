MOD = 10 ** 9 + 7


def main(s):
    reminder = [[(j - k) * 9 % 13 for j in range(10)] for k in range(13)]
    dp = [1] + [0] * 12
    for char in s:
        if char == "?":
            dp = [sum(dp[j] for j in k) % MOD for k in reminder]
        else:
            dp = [dp[(int(char) - k) * 9 % 13] for k in range(13)]

    return dp[5]


S = input()
print(main(S))
