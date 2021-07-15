import io
import os

from collections import Counter, defaultdict, deque



def solve(N, M, edges, topics):
    g = [[] for i in range(N)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    assert len(topics) == N
    vertices = sorted(list(range(N)), key=lambda k: topics[k])

    seen = set()
    for v in vertices:
        best = -1
        uniq = set()
        for nbr in g[v]:
            if nbr in seen:
                best = max(best, topics[nbr])
                uniq.add(topics[nbr])
        if best + 1 != topics[v] or len(uniq) != topics[v]:
            return -1
        seen.add(v)

    return " ".join(str(x + 1) for x in vertices)


def __starting_point():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    N, M = [int(x) for x in input().split()]
    edges = [[int(x) - 1 for x in input().split()] for i in range(M)]  # 0 indexed
    topics = [int(x) - 1 for x in input().split()]  # 0 indexed
    ans = solve(N, M, edges, topics)
    print(ans)

__starting_point()
