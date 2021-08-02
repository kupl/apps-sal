n = int(input())
x = [input().split() for i in range(n)]
for i in range(n):
    x[i].append(i + 1)
y = sorted(x, key=lambda i: (i[0], -int(i[1])))
for i in range(n):
    print(y[i][2])
