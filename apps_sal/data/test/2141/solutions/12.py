n = int(input())
m = [[''] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            m[i][j] = "W"
        else:
            m[i][j] = "B"
for i in range(n):
    print(''.join(m[i]))
