import sys
import numpy as np
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


def convolve(x, y):
    MOD = 10**9+7
    z = np.convolve(x, y) % MOD
    z[:12] += z[13:25]
    return z[:13] % MOD


def main():
    mod = 10**9+7
    S = input()[::-1]
    dp = np.zeros((len(S), 13), dtype='int64')
    amari = 1
    if S[0] == '?':
        for j in range(10):
            dp[0][j] = 1
    else:
        dp[0][int(S[0])] = 1

    for i in range(1, len(S)):
        arr = np.zeros(13, dtype='int64')
        amari = 10*amari % 13
        if S[i] == '?':
            for si in range(10):
                arr[amari*si % 13] += 1
        else:
            arr[amari*int(S[i]) % 13] = 1
        dp[i] = convolve(dp[i-1], arr)

    print(dp[len(S)-1][5])


def __starting_point():
    main()
__starting_point()
