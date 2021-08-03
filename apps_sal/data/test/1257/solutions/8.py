n, k = map(int, input().split())

sol = [[0] * n for _ in range(n)]

res = 0
c = 1
for j in range(k - 1):
    for i in range(n):
        sol[i][j] = c
        c += 1

for i in range(n):
    for j in range(k - 1, n):
        sol[i][j] = c
        c += 1

for i in range(n):
    res += sol[i][k - 1]

print(res)
for line in sol:
    for col in line:
        print(col, end=" ")
    print()
