n, m = list(map(int, input().split()))

table = []
for i in range(n):
    rows = input().split()
    rows_num = [int(x) for x in rows]
    table.append(rows_num)

isVal = False
for i in range(m):
    if table[0][i] == 1 or table[n - 1][i] == 1:
        isVal = True

for i in range(n):
    if table[i][0] == 1 or table[i][m - 1] == 1:
        isVal = True

if isVal:
    print(2)
else:
    print(4)
