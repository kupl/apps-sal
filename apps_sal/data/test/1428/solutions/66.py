from itertools import product, permutations


def main():
    N, C = list(map(int, input().split()))
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    T = [[0] * C for _ in range(3)]
    for x, y in product(list(range(N)), repeat=2):
        r = (x + y) % 3
        for i in range(C):
            T[r][i] += D[c[x][y] - 1][i]
    Q = []
    for j in range(3):
        Q.append(sorted((t, i) for i, t in enumerate(T[j])))
    m = 10**10
    for x, y, z in product(list(range(3)), repeat=3):
        X, Y, Z = Q[0][x], Q[1][y], Q[2][z]
        if X[1] == Y[1] or Y[1] == Z[1] or Z[1] == X[1]:
            continue
        m = min(m, X[0] + Y[0] + Z[0])
    return m


print((main()))
