for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    rows = 0
    for i in range(n):
        if 1 in arr[i]:
            rows += 1
    rows = n - rows

    cols = 0
    for j in range(m):
        for i in range(n):
            if arr[i][j] == 1:
                cols += 1
                break

    cols = m - cols

    if min(cols, rows) % 2 == 0:
        print("Vivek")
    else:
        print("Ashish")
