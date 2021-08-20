from fractions import gcd
import sys
sys.setrecursionlimit(10 ** 4)
num = [10 ** 9, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def main():
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [[''] * (n + 1) for _ in range(len(a))]
    dp[0][num[a[0]]] = str(a[0])
    for i in range(num[a[0]], n + 1):
        if len(dp[0][i - num[a[0]]]) > 0:
            dp[0][i] = dp[0][i - num[a[0]]] + str(a[0])
    for i in range(1, len(a)):
        for j in range(n + 1):
            if j < num[a[i]]:
                dp[i][j] = dp[i - 1][j]
            elif j == num[a[i]] or dp[i][j - num[a[i]]] != '':
                buf = dp[i][j - num[a[i]]] + str(a[i])
                if len(buf) < len(dp[i - 1][j]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = buf
            else:
                dp[i][j] = dp[i - 1][j]
    ans = list(dp[len(a) - 1][n])
    ans.sort(reverse=True)
    print(''.join(ans))


def __starting_point():
    main()


__starting_point()
