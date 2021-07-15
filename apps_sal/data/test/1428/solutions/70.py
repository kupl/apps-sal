import itertools

n, cc = list(map(int, input().split()))
d = [list(map(int, input().split())) for i in range(cc)]
c = [list(map(int, input().split())) for i in range(n)]

counter = [[0 for i in range(cc)] for j in range(3)]
for i in range(n):
    for j in range(n):
        counter[(i+j)%3][c[i][j]-1] += 1

m = 250000000
for y in itertools.permutations(range(cc), 3):
    new = 0
    for i in range(3):
        for x in range(cc):
            new += counter[i][x-1]*d[x-1][y[i]]
    m = min(m, new)

print(m)
