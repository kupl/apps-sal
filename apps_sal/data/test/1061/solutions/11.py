mat = [list(map(int, input().split())) for x in range(5)]

pos = (0, 0)
mid = (2, 2)

for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            pos = i, j

res = abs(mid[0] - pos[0]), abs(mid[1] - pos[1])
print(sum(res))
