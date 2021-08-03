import sys
from collections import deque
from operator import itemgetter
input = sys.stdin.readline


def main():
    n = int(input())
    p = [list(map(int, input().split())) + [i] for i in range(n)]
    tree = [[] for _ in range(n)]

    p.sort()
    for i in range(n - 1):
        if p[i][0] == p[i + 1][0]:
            tree[p[i][2]].append(p[i + 1][2])
            tree[p[i + 1][2]].append(p[i][2])

    p.sort(key=itemgetter(1))
    for i in range(n - 1):
        if p[i][1] == p[i + 1][1]:
            tree[p[i][2]].append(p[i + 1][2])
            tree[p[i + 1][2]].append(p[i][2])

    p.sort(key=itemgetter(2))

    already = [False] * n
    ans = -n
    for i in range(n):
        if already[i]:
            continue
        already[i] = True
        not_yet = deque([i])
        key_x = {p[i][0]}
        key_y = {p[i][1]}
        while not_yet:
            key = not_yet.popleft()
            for v in tree[key]:
                if already[v]:
                    continue
                already[v] = True
                key_x.add(p[v][0])
                key_y.add(p[v][1])
                not_yet.append(v)
        ans += len(key_x) * len(key_y)

    print(ans)


def __starting_point():
    main()


__starting_point()
