T = int(input())

for t in range(T):
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]

    rows = set()
    cols = set()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                rows.add(i)
                cols.add(j)

    m = min(n - len(rows), m - len(cols))
    if m % 2 == 0:
        print("Vivek")
    else:
        print("Ashish")
