inp = input()
inp = inp.split()
n = int(inp[0])
k = int(inp[1]) - 1

ans = 0
count = 1
table = [[0] * n for i in range(n)]

for i in range(k):
    for j in range(n):
        table[j][i] = count
        count = count + 1

for i in range(n):
    for j in range(k, n):
        table[i][j] = count
        count = count + 1

for i in range(n):
    ans = ans + table[i][k]

print(ans)

for i in table:
    for j in i:
        print(j, end=' ')
    print()
