n = int(input())
row1 = [0, 1] * (n // 2) + [0]
row2 = [1, 0] * (n // 2) + [1]

d = []
for i in range(4):
    d.append([0, 0])
    for j in range(n):
        row = [int(x) for x in input()]
        for k in range(n):
            # print(i, j, k)
            if j % 2 == 0:
                d[i][0] += abs(row1[k] - row[k])
                d[i][1] += abs(row2[k] - row[k])
            else:
                d[i][1] += abs(row1[k] - row[k])
                d[i][0] += abs(row2[k] - row[k])
    if i < 3:
        input()

# min_ = min([(d[0][0] + d[1][0] + d[2])])
m = [0] * 6
m[0] = d[0][0] + d[1][0] + d[2][1] + d[3][1]
m[1] = d[0][0] + d[1][1] + d[2][0] + d[3][1]
m[2] = d[0][0] + d[1][1] + d[2][1] + d[3][0]
m[3] = d[0][1] + d[1][0] + d[2][0] + d[3][1]
m[4] = d[0][1] + d[1][0] + d[2][1] + d[3][0]
m[5] = d[0][1] + d[1][1] + d[2][0] + d[3][0]


print(min(m))
