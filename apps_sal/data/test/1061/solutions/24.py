a = []
for i in range(0, 5):
    a.append(list(map(int, input().split())))
for i in range(0, 5):
    for j in range(0, 5):
        if a[i][j] == 1:
            print(abs(2 - i) + abs(2 - j))
