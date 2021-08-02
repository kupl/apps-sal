import sys
breadline = sys.stdin.buffer.readline
bread = sys.stdin.buffer.read
readline = sys.stdin.readline
read = sys.stdin.read
printout = sys.stdout.write
sprint = sys.stdout.flush
sys.setrecursionlimit(10 ** 7)

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7


def getnum(t=int): return t(breadline())
def numline(t=int): return map(t, breadline().split())
def numread(t=int): return map(t, bread().split())
def getstr(): return readline().strip()
def strline(): return readline().strip().split()
def strread(): return read().strip().split()


def dfs(c, to, seen):
    for n in to[c]:
        if not seen[n]:
            seen[n] = 1
            dfs(n, to, seen)


def run():
    N, M = numline()
    to = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, z = numline()
        to[x].append(y)
        to[y].append(x)

    G = []
    seen = [0] * (N + 1)
    for i in range(1, N + 1):
        if not seen[i]:
            seen[i] = 1
            dfs(i, to, seen)
            G.append(i)
    # print(G)
    print(len(G))


def __starting_point():
    run()


__starting_point()
