N = int(input())

table = [[0] * 9 for i in range(9)]

for i in range(1, N + 1):
    if int(str(i)[len(str(i)) - 1]) == 0:
        continue
    table[int(str(i)[0]) - 1][int(str(i)[len(str(i)) - 1]) - 1] += 1

ans = 0
for i in range(9):
    for j in range(i, 9):
        if i == j:
            ans += table[i][j] * table[j][i]
        else:
            ans += table[i][j] * table[j][i] * 2
print(ans)
