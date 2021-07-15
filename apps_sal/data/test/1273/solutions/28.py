
from collections import deque
def resolve():
    N = int(input())
    G = [[] for _ in range(N)]
    nextV = []

    for _ in range(N - 1):
        a, b = [int(x) - 1 for x in input().split()]
        G[a].append(b)
        nextV.append(b)

    q = deque()
    q.append(0)
    color = [0] * N
    while q:
        v = q.popleft()
        parentC = color[v]
        c = 1
        for to in G[v]:
            if c == parentC:  # 親と同じ色だったら次の色を使用
                c += 1
            color[to] = c
            c += 1
            q.append(to)

    print((max(color)))
    for b in nextV:
        print((color[b]))


def __starting_point():
    resolve()

__starting_point()
