import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def main():
    n = int(input())
    tt = LI()
    vv = LI() + [0]
    y = 0
    max_vL = [1000] * (n - 1)
    max_vR = [1000] * (n - 1)
    for i in range(n - 1):
        y = min(vv[i], vv[i + 1], y + tt[i])
        max_vL[i] = y
    y = 0
    for i in range(n - 2, -1, -1):
        y = min(vv[i + 1], vv[i], y + tt[i + 1])
        max_vR[i] = y
    yy = [0] * (n + 1)
    for i in range(n - 1):
        yy[i + 1] = min(max_vL[i], max_vR[i])
    ans = 0
    for t, y0, y1, v in zip(tt, yy, yy[1:], vv):
        h = (t + y0 + y1) / 2
        ans += ((h + y0) * (h - y0) + (h + y1) * (h - y1)) / 2
        if h > v:
            ans -= (h - v)**2
    print(ans)


main()
