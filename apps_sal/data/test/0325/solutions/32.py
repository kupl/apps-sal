import sys
sys.setrecursionlimit(1000000000)
def ii(): return int(input())
def mis(): return list(map(int, input().split()))
def lmis(): return list(mis())


def main():
    N, M, P = mis()

    to = [[] for _ in range(N)]
    ot = [[] for _ in range(N)]
    edges = []

    for i in range(M):
        a, b, c = mis()
        a -= 1
        b -= 1
        c = -(c - P)
        #
        to[a].append(b)
        ot[b].append(a)
        edges.append((a, b, c))

    reachableFrom0 = set()
    reachableToN = set()

    # dfs
    reachableFrom0.add(0)
    nodes = [0]
    while nodes:
        node = nodes.pop()
        for i in to[node]:
            if i not in reachableFrom0:
                nodes.append(i)
                reachableFrom0.add(i)

    # rdfs
    reachableToN.add(N - 1)
    nodes = [N - 1]
    while nodes:
        node = nodes.pop()
        for i in ot[node]:
            if i not in reachableToN:
                nodes.append(i)
                reachableToN.add(i)

    ok = reachableFrom0 & reachableToN

    edges = tuple((a, b, c) for a, b, c in edges if a in ok and b in ok)

    V = [float('inf')] * N
    V[0] = 0

    def bf(n):
        for _ in range(n):
            upd = False
            for a, b, c in edges:
                if V[b] > V[a] + c:
                    V[b] = V[a] + c
                    upd = True
            if not upd:
                return False
        return True

    bf(N)

    if not bf(1):
        print((max(-V[-1], 0)))
    else:
        print((-1))


main()
