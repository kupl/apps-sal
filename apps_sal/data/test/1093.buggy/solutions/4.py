(n, m) = list(map(int, input().split()))
p = []
for i in range(n):
    p.append(list(input()))
e = []
for i in range(m):
    col = 0
    for t in range(n):
        if p[t][i] == '*':
            col += 1
    e.append(col)
max1 = 0
max2 = 0
for i in range(m - 1):
    max1 = max(max1, e[i + 1] - e[i])
for i in range(1, m):
    max2 = min(max2, e[i] - e[i - 1])
print(max1, -max2)
