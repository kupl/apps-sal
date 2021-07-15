from queue import Queue
import sys

def __starting_point():

    def bfs(flag):
        vis = set()
        vis |= {1}
        q = Queue()
        q.put((1, 0))

        while not q.empty():
            u, dis = q.get()
            for v in range(1, n+1):
                if (v not in vis) and (((u, v) in h) == flag):
                    vis |= {v}
                    q.put((v, dis+1))
                    if v == n:
                        return dis+1
        return -1

    n, m = list(map(int, input().split()))

    h = set()
    for _ in range(0, m):
        x, y = list(map(int, input().split()))
        h |= {(x, y)}
        h |= {(y, x)}
    dist1 = bfs(True)
    dist2 = bfs(False)
    # print(dist1, dist2)
    if dist1 == -1 or dist2 == -1:
        print(-1)
    else:
        print(max(dist1, dist2))

__starting_point()
