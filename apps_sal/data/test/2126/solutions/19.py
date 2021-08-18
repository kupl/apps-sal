n, m, h = list(map(int, input().split()))

front = [int(x) for x in input().split()]
left = [int(x) for x in input().split()]

top = [[int(x) for x in input().split()] for _ in range(n)]

box = [[[top[nn][mm]] * h for mm in range(m)] for nn in range(n)]

for j in range(m):
    for i in range(n):
        for z in range(front[j], h):
            box[i][j][z] = 0

for i in range(n):
    for j in range(m):
        for z in range(left[i], h):
            box[i][j][z] = 0

for i in range(n):
    print(' '.join(str(sum(box[i][j])) for j in range(m)))
