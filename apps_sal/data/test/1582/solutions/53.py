n = int(input())
lst = [[0 for i in range(9)] for j in range(9)]
for i in range(1, n + 1):
    s = str(i)
    if i % 10:
        lst[int(s[0]) - 1][i % 10 - 1] += 1
res = 0
for i in range(9):
    for j in range(9):
        res += lst[i][j] * lst[j][i]
print(res)
