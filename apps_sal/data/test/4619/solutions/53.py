w, h, n = map(int, input().split())
l = [[0] * w for _ in range(h)]
count = 0
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(h):
            for j in range(x):
                if l[i][j] == 0:
                    l[i][j] = 1
                    count += 1
    if a == 2:
        for i in range(h):
            for j in range(x, w):
                if l[i][j] == 0:
                    l[i][j] = 1
                    count += 1
    if a == 3:
        for i in range(y):
            for j in range(w):
                if l[i][j] == 0:
                    l[i][j] = 1
                    count += 1
    if a == 4:
        for i in range(y, h):
            for j in range(w):
                if l[i][j] == 0:
                    l[i][j] = 1
                    count += 1

print(w * h - count)
