n, m = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(m)]


def shortest_path(s):
    MIN = -1 * 10 ** 12
    d = [MIN] * (n + 1)
    d[s] = 0
    update = True
    cnt = 1
    tmp = MIN
    while update:
        update = False
        for a, b, c in graph:
            if d[a] != MIN and d[b] < d[a] + c:
                d[b] = d[a] + c
                update = True
        if cnt == m: tmp = d[n]
        if update and cnt == 2 * m and d[n] > tmp: return 'inf'
        if cnt == 2 * m: update = False
        cnt += 1
    return d[n]


print(shortest_path(1))
