import sys,math,copy

def main():
    # import numpy as np
    input = sys.stdin.readline
    S = ''.join(reversed(input().strip()))

    # dp = np.zeros((13), dtype=int)
    # dp_ = np.zeros((13), dtype=int)
    dp = [0] * 13
    dp_ = [0] * 13
    mod13_list = [i % 13 for i in range(12 ** 2 + 1)]
    list10 = list(range(10))
    list13 = list(range(13))
    divisor = 10 ** 9 + 7
    dp_[0] = 1
    mul = 1
    for i in range(len(S)):
        s = S[i]
        if s == '?':
            for d in list10:
                m = mod13_list[(d * mul)]
                for pm in list13:
                    dp[mod13_list[(pm+m)]] += dp_[pm]

        else:
            si = int(s)
            m = mod13_list[(si * mul)]
            for pm in list13:
                dp[mod13_list[(pm+m)]] = dp_[pm]

        # dp_ = dp % divisor
        # dp = dp * 0 # np.zeros((13), dtype=int)
        for j in list13:
            dp_[j] = dp[j] % divisor
            dp[j] = 0
        mul = mod13_list[(mul * 10)]
    print(dp_[5])

main()
