
n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))


def check(x, y):
    for i in range(n):
        k = 0
        for j in range(m):
            if (j == x):
                if (a[i][y] != j + 1):
                    k += 1
            elif (j == y):
                if (a[i][x] != j + 1):
                    k += 1
            elif (a[i][j] != j + 1):
                k += 1
        if k > 2:
            return False
    return True


for e in range(m):
    for r in range(m):
        if check(e, r):
            print('YES')
            return
print('NO')
