from itertools import permutations
n, c = list(map(int, input().split()))
D = [tuple(map(int, input().split())) for _ in range(c)]
C = [tuple([int(x) - 1 for x in input().split()]) for _ in range(n)]

cols = [[0] * c for _ in range(3)]
for i in range(n):
    for j in range(n):
        c_from = C[i][j]
        cols[(i + j) % 3][c_from] += 1

d = 1000 * 500 * 500
for p0, p1, p2 in permutations(list(range(c)), 3):
    d_ = 0
    for c_from in range(c):
        d_ += cols[0][c_from] * D[c_from][p0]
        d_ += cols[1][c_from] * D[c_from][p1]
        d_ += cols[2][c_from] * D[c_from][p2]
    d = min(d, d_)
print(d)
