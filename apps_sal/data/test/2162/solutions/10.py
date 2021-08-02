from sys import stdin, stdout

inf = 1000000000000007


def solve():
    a1, b1, c1 = [int(i) for i in stdin.readline().split()]
    k = a1 + b1 + c1;
    a = [0 for i in range(k + 1)]
    for i in stdin.readline().split():
        a[int(i)] = 0
    for i in stdin.readline().split():
        a[int(i)] = 1
    for i in stdin.readline().split():
        a[int(i)] = 2
    dp = [[inf for i in range(k + 1)] for j in range(3)]
    dp[0][0], dp[1][0], dp[2][0] = 0, 0, 0
    for i in range(1, k + 1):
        for j in range(3):
            if(a[i] == j):
                for l in range(0, j + 1):
                    dp[j][i] = min(dp[j][i], dp[l][i - 1])
            else:
                for l in range(0, j + 1):
                    dp[j][i] = min(dp[j][i], dp[l][i - 1] + 1)
    print(min(dp[0][k], dp[1][k], dp[2][k]))


solve()
