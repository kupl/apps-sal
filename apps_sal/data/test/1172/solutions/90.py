#!/usr/bin/env python3


def main():
    S = input()
    N = len(S)
    m = 10**9 + 7
    # dp[i][j]:= 先頭からi-1文字目までみてABCのうちj文字目まで選んでいた時の残りの処理の個数
    dp = [[0]*4 for _ in range(N+1)]
    for i in range(N,-1,-1):
        for j in range(3,-1,-1):
            # print(i,j)
            if i == N:
                if j == 3:
                    # print(i,j)
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                if S[i] == '?':
                    dp[i][j] = dp[i+1][j] * 3 % m
                else:
                    dp[i][j] = dp[i+1][j]
                
                if j < 3:# S[i]文字を選択する場合
                    if S[i] == '?' or S[i] == 'ABC'[j]:
                        dp[i][j] += dp[i+1][j+1]
                        dp[i][j] %= m

    print((dp[0][0]))


def __starting_point():
    main()

__starting_point()
