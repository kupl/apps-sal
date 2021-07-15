import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n, k = MI()
    xy = []
    xx = []
    yy = []
    for _ in range(n):
        x, y = MI()
        xy.append([x, y])
        xx.append(x)
        yy.append(y)
    xx.sort()
    yy.sort()
    #print(xx)
    #print(yy)
    xtoi = {x: i for i, x in enumerate(xx)}
    ytoj = {y: j for j, y in enumerate(yy)}
    cs2d = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in xy:
        i, j = xtoi[x], ytoj[y]
        cs2d[i + 1][j + 1] = 1
    #p2D(cs2d)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cs2d[i][j] += cs2d[i][j - 1]
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            cs2d[i][j] += cs2d[i-1][j]
    #p2D(cs2d)
    ans = 10 ** 20
    for ri in range(n):
        r = xx[ri]
        for li in range(ri):
            l = xx[li]
            for ti in range(n):
                t = yy[ti]
                for bi in range(ti):
                    b = yy[bi]
                    cnt = cs2d[ri+1][ti+1]-cs2d[ri+1][bi]-cs2d[li][ti+1]+cs2d[li][bi]
                    if cnt >= k:
                        s = (r - l) * (t - b)
                        if s < ans: ans = s
    print(ans)

main()

