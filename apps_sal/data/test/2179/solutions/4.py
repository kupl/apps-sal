from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappop, heappush
import bisect
import sys
import threading


def main():
    (n, m) = map(int, input().split())
    adj = [[] for i in range(n + 1)]
    for i in range(m):
        (a, b, c) = map(int, input().split())
        adj[a].append((b, c, i))
        adj[b].append((a, c, i))
    v = int(input())
    (visited, ans, tw) = ([0] * (n + 1), [], 0)
    Q = [(0, 0, v, 0)]
    while Q:
        (w, lew, u, ei) = heappop(Q)
        if visited[u]:
            continue
        visited[u] = 1
        ans.append(str(ei + 1))
        tw += lew
        for (to, we, eii) in adj[u]:
            if not visited[to]:
                heappush(Q, (we + w, we, to, eii))
    print(tw)
    print(' '.join(ans[1:]))


def __starting_point():
    sys.setrecursionlimit(200000)
    threading.stack_size(102400000)
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
