row, col = list(map(int, input().split()))
a = []
x = [0] * row
y = [0] * col
for i in range(row):
    s = input()
    a.append(s)
total = 0
for i in range(row):
    for j in range(col):
        if a[i][j] == "*":
            x[i] += 1
            y[j] += 1
            total += 1
for i in range(row):
    for j in range(col):
        if (x[i] + y[j] - (a[i][j] == "*")) == total:
            print("YES")
            print(i + 1, j + 1)
            return
print("NO")
