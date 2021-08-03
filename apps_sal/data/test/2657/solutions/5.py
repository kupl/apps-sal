n = int(input())
a = list(map(int, input().split()))
ma = max(a)
a = a[:a.index(ma)] + a[a.index(ma) + 1:]
l = []
for i in range(n - 1):
    l.append([abs(ma - 2 * a[i]), "-" if ma - 2 * a[i] >= 0 else "+"])
l.sort()
print(ma, end=" ")
print((ma - l[0][0]) // 2) if l[0][1] == "-" else print((ma + l[0][0]) // 2)
