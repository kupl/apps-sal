import sys, itertools
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    H, W = LI()
    s = [list(S()) for _ in range(H)]

    for i, j in itertools.product(list(range(H)), list(range(W))):
        if s[i][j] != '#':
            cnt = 0
            for k, l in itertools.product(list(range(-1, 2)), repeat=2):
                if 0 <= i + k < H and 0 <= j + l < W:
                    if s[i+k][j+l] == '#':
                        cnt += 1
            s[i][j] = str(cnt)

    for i in s:
        print((''.join(i)))

def __starting_point():
    resolve()

__starting_point()
