import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A, G, C, T = 0, 1, 2, 3
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for j in range(4):  # i - 2 文字目
        for k in range(4):  # i - 1 文字目
            for l in range(4):  # i 文字目
                if j == A and k == G and l == C:  continue
                if j == A and k == C and l == G:  continue
                if j == G and k == A and l == C:  continue
                dp[3][j][k][l] = 1
    
    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == A and k == G and l == C:  continue
                        if j == A and k == C and l == G:  continue
                        if j == G and k == A and l == C:  continue
                        if m == A and k == G and l == C:  continue
                        if m == A and j == G and l == C:  continue
                        dp[i][j][k][l] += dp[i-1][m][j][k]
                        dp[i][j][k][l] %= MOD
    
    res = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                res += dp[N][j][k][l]
                res %= MOD
    
    print(res)

def __starting_point():
    main()
__starting_point()
