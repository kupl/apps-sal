import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def solve(n, m, g):
    dp = [0] * n
    ans = []
    for i in range(n):
        for w in g[i]:
            dp[i] = max(dp[i], dp[w] + 1)
        if dp[i] >= 2:
            dp[i] = -1
            ans.append(i+1)
    wi(len(ans))
    wia(ans)


def main():
    for _ in range(ri()):
        n, m = ria()
        g = [[] for i in range(n)]
        for __ in range(m):
            u, v = ria()
            g[v-1].append(u-1)
        solve(n, m, g)


def __starting_point():
    main()

__starting_point()
