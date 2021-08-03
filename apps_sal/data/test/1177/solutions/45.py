import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    md = 998244353
    n, s = MI()
    aa = LI()
    dp = [0] * (s + 1)
    ans = 0
    for a in aa:
        dp[0] += 1
        for i in range(s, a - 1, -1):
            dp[i] += dp[i - a]
            dp[i] %= md
        ans += dp[s]
        ans %= md
    print(ans)


main()
