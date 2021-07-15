n = int(input())
a = [int(i) for i in input().split()]
box = [[0]*100 for i in range(n)]
for i in range(n):
    for j in range(a[i]):
        box[i][j] = 1
rows = []
for i in range(max(a)):
    row = 0
    for j in range(n):
        if box[j][i] == 1:
            row += 1
    rows.append(row)
for i in range(1, n+1):
    for j in range(len(rows)):
        if i <= rows[j]:
            box[-i][j] = 1
        else:
            box[-i][j] = 0
ans = ''
for collumn in box:
    ans += str((sum(collumn))) + ' '
print(ans[:-1])

