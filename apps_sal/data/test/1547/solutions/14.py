def fill_column(num, color):
    nonlocal canvas
    for i in range(n):
        canvas[i][num] = color


def fill_row(num, color):
    nonlocal canvas
    for i in range(m):
        canvas[num][i] = color


(n, m, k) = map(int, input().split())
canvas = [[0 for j in range(m)] for i in range(n)]
(T, num, color) = (0, 0, 0)
a = []
T1 = [-1 for i in range(n)]
T2 = [-1 for j in range(m)]
for i in range(k):
    (T, num, color) = map(int, input().split())
    a.append((T, num - 1, color))
    if T == 1:
        T1[num - 1] = i
    else:
        T2[num - 1] = i

for i in range(k):
    if a[i][0] == 1:
        if T1[a[i][1]] == i:
            fill_row(a[i][1], a[i][2])
    else:
        if T2[a[i][1]] == i:
            fill_column(a[i][1], a[i][2])

for i in range(n):
    for j in range(m):
        print(canvas[i][j], end=' ')
    print()
