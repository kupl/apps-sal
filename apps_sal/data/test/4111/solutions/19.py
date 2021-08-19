n = int(input())
a = list(map(int, input().split()))
o = [a[0]]
e = [0]
for i in range(1, n):
    o.append(o[i - 1] if i % 2 == 1 else o[i - 1] + a[i])
    e.append(e[i - 1] if i % 2 == 0 else e[i - 1] + a[i])
c = 0
for i in range(1, n):
    od = o[i] - a[i] + e[-1] - e[i - 1]
    ev = e[i] - a[i] + o[-1] - o[i - 1]
    if od == ev:
        c += 1
se = so = 0
for i in range(n):
    se += a[i] if i % 2 == 1 else 0
    so += a[i] if i % 2 == 0 else 0
if se == so - a[0]:
    c += 1
print(c)
