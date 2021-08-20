from collections import deque
import sys
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(ns())


def na():
    return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    g = [list() for _ in range(n)]
    to = list()
    for i in range(n - 1):
        (a, b) = na()
        a -= 1
        b -= 1
        g[a].append(b)
        to.append(b)
    l = [-1] * n
    l[0] = 10 ** 10
    q = deque([0])
    while q:
        v = q.popleft()
        vcolor = l[v]
        for (i, w) in enumerate(g[v]):
            q.append(w)
            if i < vcolor:
                l[w] = i
            else:
                l[w] = i + 1
    print(max(l[1:]) + 1)
    for i in to:
        print(l[i] + 1)


def __starting_point():
    main()


__starting_point()
