m, n, k = list(map(int, input().split()))
Matrix = []
for i in range(m):
    s =  input()
    Matrix.append([])
    for j in range(n):
        if s[j] == '*':
            Matrix[i].append(0)
        else:
            Matrix[i].append(1)
count = 0
for i in range(m):
    res = 0
    for j in range(n):
        if Matrix[i][j]:
            res += 1
            if res >= k:
                count += 1
        else:
            res = 0

for i in range(n):
    res = 0
    for j in range(m):
        if Matrix[j][i]:
            res += 1
            if res >= k:
                count += 1
        else:
            res = 0
if k == 1:
    count //= 2

print(count)

