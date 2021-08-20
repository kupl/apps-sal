n = int(input())
t = list(map(int, input().split()))
a = []
b = []
c = []
for (i, m) in enumerate(t):
    if m == 1:
        a.append(i + 1)
    elif m == 2:
        b.append(i + 1)
    else:
        c.append(i + 1)
w = min([len(a), len(b), len(c)])
print(w)
for i in range(w):
    print(a[i], b[i], c[i])
