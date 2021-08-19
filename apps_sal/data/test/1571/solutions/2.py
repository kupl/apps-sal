import sys


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def main():
    md = 998244353
    s = SI()
    t = SI()
    sn = len(s)
    tn = len(t)
    dp = [[0] * sn for _ in range(sn + 1)]
    for j in range(sn):
        dp[1][j] = 2 if j >= tn or t[j] == s[0] else 0
    for (i, c) in enumerate(s[1:], 1):
        for j in range(sn):
            pre = dp[i][j]
            if pre == 0:
                continue
            if j > 0 and (j - 1 >= tn or t[j - 1] == c):
                dp[i + 1][j - 1] = (dp[i + 1][j - 1] + pre) % md
            if j + i < sn and (j + i >= tn or t[j + i] == c):
                dp[i + 1][j] = (dp[i + 1][j] + pre) % md
    ans = sum((dp[i][0] for i in range(tn, sn + 1))) % md
    print(ans)


main()
