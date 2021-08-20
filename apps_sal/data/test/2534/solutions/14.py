(r, c) = map(int, input().strip().split())
main = []
row = []
col = []
for j in range(r):
    a = list(map(int, input().strip().split()))
    main.append(a)
    row.append(min(a))
count = 0
for i in range(c):
    max = 0
    for k in range(r):
        if max < main[k][i]:
            max = main[k][i]
    col.append(max)
for i in range(r):
    n = row[i]
    for j in range(c):
        if main[i][j] == n and col[j] == n:
            count = 1
            break
    if count == 1:
        print(n)
        break
if count == 0:
    print('GUESS')
