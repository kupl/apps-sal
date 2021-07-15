from  collections import Counter

n = int(input())
v = list(map(int, input().split()))

c = Counter(v[::2])
d = Counter(v[1::2])

x = c.most_common()
y = d.most_common()

s = 0

if x[0][0] == y[0][0]:
    if len(x) > 1 and len(y) > 1:
        s = min(n - x[0][1] - y[1][1], n - x[1][1] - y[0][1])
    elif len(x) > 1:
        s = n - x[1][1] - y[0][1]
    elif len(y) > 1:
        s = n - x[0][1] - y[1][1]
    else:
        s = n // 2
else:
    s = n - x[0][1] - y[0][1]

print(s)
