from collections import defaultdict
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n, x, y = list(map(int, input().split()))
    edges = {e: [] for e in range(n)}
    for i1 in range(1, n - 1):
        edges[i1].append(i1 - 1)
        edges[i1].append(i1 + 1)
    edges[0].append(1)
    edges[n - 1].append(n - 2)
    edges[x - 1].append(y - 1)
    edges[y - 1].append(x - 1)

    dis = defaultdict(int)
    for j1 in range(n):
        seen = set()
        cnt = 0
        dis_each = [n] * n
        nexts = [j1]
        nextnext = []
        while len(seen) < n:
            for next in nexts:
                if next not in seen:
                    seen.add(next)
                    dis_each[next] = cnt
                    nextnext += edges[next]
            nexts = nextnext
            nextnext = []
            cnt += 1
        for d in dis_each:
            dis[d] += 1
    for k1 in range(1, n):
        print((dis[k1] // 2))


def __starting_point():
    main()


__starting_point()
