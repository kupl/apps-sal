n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i] = list(input())
c1 = 0
for i in range(n):
    c = 0
    for j in range(n):
        if a[i][j] == 'C':
            c += 1
    c1 += c * (c - 1) // 2
for i in range(n):
    c = 0
    for j in range(n):
        if a[j][i] == 'C':
            c += 1
    c1 += c * (c - 1) // 2
print(c1)
