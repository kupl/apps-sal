n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]


def distance(x, y, i, j):
    return abs(x - i) + abs(y - j)


for a, b in ab:
    dists = [distance(a, b, c, d) for c, d in cd]
    print(dists.index(min(dists)) + 1)
