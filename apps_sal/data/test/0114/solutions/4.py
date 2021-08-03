n, m = list(map(int, input().split()))
ar = []
for x in range(n):
    e = list(map(int, input().split()))
    ar.append(e)
col = set()
moves = []
for i in range(n - 1):
    for j in range(m - 1):
        if(ar[i][j] == ar[i + 1][j] == ar[i][j + 1] == ar[i + 1][j + 1] == 1):
            moves.append([i + 1, j + 1])
            col.add((i, j))
            col.add((i + 1, j))
            col.add((i + 1, j + 1))
            col.add((i, j + 1))
for i in range(n):
    for j in range(m):
        if(ar[i][j]):
            if((i, j) not in col):
                print(-1)
                quit()
print(len(moves))
for x in moves:
    print(*x)
