N = int(input())
m = 0
x = [[0] * 9 for i in range(9)]
for i in range(1, N + 1):
    if i % 10 == 0:
        continue
    b = int(str(i)[0])
    g = int(i % 10)
    x[b - 1][g - 1] += 1
ans = 0
for i in range(9):
    for j in range(9):
        ans += x[i][j] * x[j][i]
print(ans)
