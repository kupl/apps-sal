import sys
import collections
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def main():
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    q = [collections.deque() for j in range(N)]
    for (i, a) in enumerate(A):
        for aa in a:
            q[i].append(aa)
    ans = 0
    current = defaultdict(int)
    for (i, v) in enumerate(q):
        current[i + 1] = v[0]
    while True:
        v = set()
        for k in list(current.keys()):
            if k == q[current[k] - 1][0]:
                v.add(k)
                v.add(current[k])
        current = defaultdict(int)
        if len(v) == 0:
            break
        for vv in v:
            q[vv - 1].popleft()
            if len(q[vv - 1]):
                current[vv] = q[vv - 1][0]
        ans += 1
    size = 0
    for i in range(N):
        size += len(q[i])
    if size == 0:
        print(ans)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
