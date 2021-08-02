n = int(input())
for i in range(n):
    if (i):
        input()
    x1 = y1 = x2 = y2 = 0
    s = [input() for i in range(8)]
    for i in range(8):
        for j in range(8):
            if (s[i][j] == 'K'):
                x1, y1, x2, y2 = x2, y2, i, j
    if (abs(x1 - x2) % 4 == 0 and abs(y1 - y2) % 4 == 0):
        print("YES")
    else:
        print("NO")
