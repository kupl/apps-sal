t = int(input())
for q in range(t):
    (n, m) = [int(i) for i in input().split()]
    a = [[int(j) for j in input().split()] for i in range(n)]
    row = [False for i in range(n)]
    col = [False for i in range(m)]
    (nr, nc) = (0, 0)
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                if not row[i]:
                    row[i] = True
                    nr += 1
                if not col[j]:
                    col[j] = True
                    nc += 1
    t = min(n - nr, m - nc)
    res = 'Vivek' if t % 2 == 0 else 'Ashish'
    print(res)
