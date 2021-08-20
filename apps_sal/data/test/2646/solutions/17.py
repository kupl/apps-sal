from collections import deque
INF = 1000000000


def main():
    (n, m) = map(int, input().split(' '))
    to = [[] for _ in range(n)]
    for _ in range(m):
        (a, b) = map(lambda i: int(i) - 1, input().split(' '))
        to[a].append(b)
        to[b].append(a)
    que = deque()
    d = {i: INF for i in range(n)}
    prev = {i: -1 for i in range(n)}
    d[0] = 0
    que.append(0)
    while que:
        v = que.popleft()
        for i in to[v]:
            if d[i] != INF:
                continue
            d[i] = d[v] + 1
            prev[i] = v
            que.append(i)
    print('Yes')
    for i in range(n):
        if i == 0:
            continue
        print(prev[i] + 1)


def __starting_point():
    main()


__starting_point()
