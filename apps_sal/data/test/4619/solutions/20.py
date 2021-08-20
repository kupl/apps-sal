(w, h, n) = [int(i) for i in input().split()]
list_2d = [[0] * w for i in range(h)]


def nurie(x, y, a):
    if a == 1:
        for i in range(h):
            for j in range(x):
                list_2d[i][j] = 1
    elif a == 2:
        for i in range(h):
            for j in range(x, w):
                list_2d[i][j] = 1
    elif a == 3:
        for i in range(y):
            for j in range(w):
                list_2d[i][j] = 1
    else:
        for i in range(y, h):
            for j in range(w):
                list_2d[i][j] = 1
    return list_2d


for i in range(n):
    (x, y, a) = [int(i) for i in input().split()]
    nurie(x, y, a)
sum = 0
for i in range(h):
    sum += list_2d[i].count(0)
print(sum)
