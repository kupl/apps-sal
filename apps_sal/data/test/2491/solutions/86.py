import sys
sys.setrecursionlimit(10 ** 8)
INF = 10 ** 15

class edge:
    def __init__(self, fr, to, cost):
        self.fr, self.to, self.cost = fr, to, cost

def input(): return sys.stdin.readline().strip()
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M = ZZ()
    es = []
    for _ in range(M):
        a, b, c = ZZ()
        a -= 1
        b -= 1
        es.append(edge(a, b, -c))

    #負の閉路検出
    d = [0] * N
    for i in range(N):
        for e in es:
            if d[e.to] > d[e.fr] + e.cost:
                d[e.to] = d[e.fr] + e.cost
                if e.to == N-1 and i == N-1:
                    print('inf')
                    return
    #ベルマンフォードする
    d = [INF] * N
    d[0] = 0
    for _ in range(N-1):
        update = False
        for e in es:
            if d[e.fr] != INF and d[e.to] > d[e.fr] + e.cost:
                d[e.to] = d[e.fr] + e.cost
                update = True
        if not update: break
    print((-d[N-1]))

    return

def __starting_point():
    main()

__starting_point()
