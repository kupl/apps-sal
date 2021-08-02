
import sys
import threading
from collections import defaultdict

n, x, y = list(map(int, input().split()))
adj = defaultdict(list)
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)


def fun(node, par, dest, ans):
    cnt = 1
    for ch in adj[node]:
        if ch != par:
            cnt += fun(ch, node, dest, ans)
    if node == dest:
        ans[0] = cnt * ans[0]
    return cnt


def main():
    ans = [1]
    t = fun(x, 0, y, ans)
    fun(y, 0, x, ans)
    print(t * (t - 1) - ans[0])


def __starting_point():
    sys.setrecursionlimit(10**6)
    threading.stack_size(10**8)
    t = threading.Thread(target=main)
    t.start()
    t.join()


__starting_point()
