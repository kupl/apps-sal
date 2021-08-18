import sys


def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    inf = 10**9
    for _ in range(II()):
        n = II()
        s = SI()
        t = SI()

        cnts = [[0] * 26 for _ in range(n + 1)]
        cntt = [[0] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            cnts[i][ord(s[i]) - 97] += 1
            cntt[i][ord(t[i]) - 97] += 1
            for j in range(26):
                cnts[i][j] += cnts[i + 1][j]
                cntt[i][j] += cntt[i + 1][j]

        ng = False
        for j in range(26):
            if cnts[0][j] != cntt[0][j]:
                ng = True
                break
        if ng:
            print(-1)
            continue

        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(n + 1):
            for j in range(i, n + 1):
                if i == n and j == n:
                    break
                pre = dp[i][j]
                if pre == inf:
                    continue
                if i < j and i + 1 <= n:
                    dp[i + 1][j] = min(dp[i + 1][j], pre + 1)
                if i + 1 <= n and j + 1 <= n and s[i] == t[j]:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], pre)
                if j + 1 <= n and cnts[i + 1][ord(t[j]) - 97] > cntt[j + 1][ord(t[j]) - 97]:
                    dp[i][j + 1] = min(dp[i][j + 1], pre)
        print(dp[n][n])


main()
