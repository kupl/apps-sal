(n, m, k) = map(int, input().split())
a = [(0, -1)] * n
b = [(0, -1)] * m
for i in range(k):
    (t, pl, col) = map(int, input().split())
    if t == 1:
        a[pl - 1] = (col, i)
    else:
        b[pl - 1] = (col, i)
for i in range(n):
    for j in range(m):
        if a[i][1] > b[j][1]:
            print(a[i][0], end=' ')
        else:
            print(b[j][0], end=' ')
    print()
