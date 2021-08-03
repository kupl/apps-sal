

for _ in range(int(input())):
    n, m = map(int, input().split())

    a = []

    for i in range(n):
        a.append(list(map(int, input().split())))

    row = [0] * n
    col = [0] * m

    for i in range(n):
        for j in range(m):
            if(a[i][j]):
                row[i] = 1
                col[j] = 1

    rowc = row.count(0)
    colc = col.count(0)

    moves = min(rowc, colc)

    if(moves & 1):
        print("Ashish")
    else:
        print("Vivek")
