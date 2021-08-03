data = [list(map(int, input().split())) for i in range(3)]
print(3)
for i in range(3):
    print(data[i][0] + data[(i + 1) % 3][0] - data[(i + 2) % 3][0], data[i][1] + data[(i + 1) % 3][1] - data[(i + 2) % 3][1])
