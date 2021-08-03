n = int(input())
e = 0
a = []
b = [[] for i in range(1001)]
for i in range(n):
    s, t = map(int, input().split())
    a.append([i, s])
    b[t].append(i)
for i in range(len(a)):
    c1 = 0
    for j in range(len(b[a[i][1]])):
        if (b[a[i][1]][j] != i):
            c1 = -1
    if (c1 != -1):
        e = e + 1
print(e)
