#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    CAA = input()
    CAB = input()
    CBA = input()
    CBB = input()
    dp = [0]*(n+1)
    dp[2] = 1
    mod = 10**9+7
    for i in range(3, n+1):
        if CAB == 'A':
            if CAA == 'A':
                dp[i] = dp[i-1]
            elif CAB == 'B' or CBA == 'B':
                dp[i] = sum(dp[:i]) % mod
            else:
                dp[i] = dp[i-1]+dp[i-2]
                dp[i] %= mod
        else:
            if CBB == 'B':
                dp[i] = dp[i-1]
            elif CAB == 'A' or CBA == 'A':
                dp[i] = sum(dp[:i]) % mod
            else:
                dp[i] = dp[i-1]+dp[i-2]
                dp[i] %= mod
    print(dp[n])


def __starting_point():
    main()
__starting_point()
