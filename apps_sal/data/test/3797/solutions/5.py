import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def main():
    md = 10 ** 9 + 7
    (n, m) = MI()
    rtol = defaultdict(list)
    for _ in range(m):
        (l, r, x) = MI()
        rtol[r].append([l, x])
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for k in range(1, n + 1):
        for i in range(k - 1):
            dp[i][k - 1] = dp[k - 1][i] = sum(dp[i][:k - 1]) % md
        for (l, x) in rtol[k]:
            if x == 1:
                for i in range(l, k):
                    for j in range(k):
                        dp[i][j] = dp[j][i] = 0
            if x == 2:
                for i in range(l, k):
                    for j in range(i + 1, k):
                        dp[i][j] = dp[j][i] = 0
                for i in range(l):
                    for j in range(i + 1):
                        dp[i][j] = dp[j][i] = 0
            if x == 3:
                for i in range(l):
                    for j in range(k):
                        dp[i][j] = dp[j][i] = 0
    print(sum((sum(dr) for dr in dp)) * 3 % md)


main()
