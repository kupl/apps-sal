(n, m, k) = map(int, input().split())
l = [[0, 0] for i in range(n + 1)]
c = [[0, 0] for i in range(m + 1)]
for i in range(k):
    (dim, ind, col) = map(int, input().split())
    ind -= 1
    if dim == 1:
        l[ind][0] = col
        l[ind][1] = i
    else:
        c[ind][0] = col
        c[ind][1] = i
for i in range(n):
    for j in range(m):
        if l[i][1] > c[j][1]:
            print(l[i][0], end=' ')
        elif l[i][1] < c[j][1]:
            print(c[j][0], end=' ')
        elif l[i][0] != 0:
            print(l[i][0], end=' ')
        else:
            print(c[j][0], end=' ')
    print()
