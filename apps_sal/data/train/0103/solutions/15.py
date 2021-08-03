t = int(input())

for _ in range(t):
    n, m = list(map(int, input().strip().split()))

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))

    rows = 0
    for row in matrix:
        if sum(row) == 0:
            rows += 1

    cols = 0
    for i in range(m):
        s = 0
        for j in range(n):
            s += matrix[j][i]
        if s == 0:
            cols += 1

    mini = min(cols, rows)

    if mini % 2 == 1:
        print("Ashish")
    else:
        print("Vivek")
