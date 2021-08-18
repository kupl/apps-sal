from sys import stdin


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x


def solve():

    N, M = map(int, stdin.readline().split())

    parent = list(range(N + 1))

    for _ in range(M):
        group = [int(k) for k in stdin.readline().split()][1:]
        if group:
            p = find(parent, group[0])

            for x in group[1:]:
                parent[find(parent, x)] = p

    cnt = [0] * (N + 1)

    for i in range(1, N + 1):
        cnt[find(parent, i)] += 1

    print(' '.join(map(str, [cnt[find(parent, i)] for i in range(1, N + 1)])))


def __starting_point():
    solve()


__starting_point()
