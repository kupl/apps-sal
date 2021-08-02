n = int(input())
l = list(map(int, input().split()))
a = list()
b = list()
for i in l:
    if i % 2:
        a.append(i)
    else:
        b.append(i)
a.sort()
b.sort()
a.reverse()
b.reverse()
k = min(len(a), len(b))
if abs(len(a) - len(b)) < 2:
    print(0)
else:
    s = 0
    if len(a) < len(b):
        for i in range(k + 1, len(b)):
            s += b[i]
    else:
        for i in range(k + 1, len(a)):
            s += a[i]
    print(s)
