q, w = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
d = []
k = 0
for i in range(0, q + w):
    if (s[i]):
        d.append(a[i])
        k = i
d.append(100000000000)
t = 0
t1 = 1
g = 0
for i in a:
    if (i == d[t]):
        continue
    elif (i - d[t] <= d[t1] - i):
        g += 1
    else:
        print(g, end=" ")
        if (d[t1] == i):
            g = 0
        else:
            g = 1
        t += 1
        t1 += 1
print(g)
