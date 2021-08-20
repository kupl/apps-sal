import sys
import math
import copy


def main():
    input = sys.stdin.readline
    S = ''.join(reversed(input().strip()))
    dp = [0] * 13
    dp_ = [0] * 13
    mod13_tuple = tuple([i % 13 for i in range(12 ** 2 + 1)])
    tuple10 = tuple(range(10))
    tuple13 = tuple(range(13))
    divisor = 10 ** 9 + 7
    dp_[0] = 1
    mul = 1
    for i in range(len(S)):
        s = S[i]
        if s == '?':
            for d in tuple10:
                m = mod13_tuple[d * mul]
                for pm in tuple13:
                    dp[mod13_tuple[pm + m]] += dp_[pm]
        else:
            si = int(s)
            m = mod13_tuple[si * mul]
            for pm in tuple13:
                dp[mod13_tuple[pm + m]] = dp_[pm]
        for j in tuple13:
            dp_[j] = dp[j] % divisor
            dp[j] = 0
        mul = mod13_tuple[mul * 10]
    print(dp_[5])


main()
