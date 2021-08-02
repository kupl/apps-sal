row, col = map(int, input().split())
a = []
for i in range(row):
    s = input()
    a.append(s)

x = [i.count("*") for i in a]
# print(x)

ao = []
for i in range(col):
    new = ""
    for j in range(row):
        new += a[j][i]
    ao.append(new)
y = [i.count("*") for i in ao]
# print(y)

total = sum(x)

for i in range(row):
    for j in range(col):
        cnt = x[i] + y[j]
        if a[i][j] == "*":
            cnt -= 1
        if total == cnt:
            print("YES")
            print(i + 1, j + 1)
            return
print("NO")
