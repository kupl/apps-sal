import sys
import threading
from collections import defaultdict


adj = defaultdict(list)
n = int(input())
for _ in range(n - 1):
    x, y, b = list(map(int, input().split()))
    adj[x].append((y, b))
    adj[y].append((x, b))


def fun(node, par, x):
    y = x
    for ch, b in adj[node]:
        if ch != par:
            y = max(fun(ch, node, x + b), y)
    return y


def main():
    print(fun(0, -1, 0))


def __starting_point():
    sys.setrecursionlimit(10**6)
    threading.stack_size(10**8)
    t = threading.Thread(target=main)
    t.start()
    t.join()


__starting_point()
