import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def main():
    n, lim = MI()
    ww = []
    vv = []
    for _ in range(n):
        w, v = MI()
        ww.append(w)
        vv.append(v)
    w0 = ww[0]
    dp = [[0] * (3 * n + 1) for _ in range(n + 1)]
    for w, v in zip(ww, vv):
        for i in range(n, 0, -1):
            sj = min(lim - i * w0, 3 * n)
            for j in range(sj, -1, -1):
                nj = j - (w - w0)
                if nj < 0:
                    break
                dp[i][j] = max(dp[i][j], dp[i - 1][nj] + v)
    print(max(max(row) for row in dp))


main()
