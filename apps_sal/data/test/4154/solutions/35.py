(n, m) = map(int, input().split())
a = []
b = []
for i in range(m):
    (l, r) = map(int, input().split())
    a.append(l)
    b.append(r)
x = max(a)
y = min(b)
if y - x < 0:
    print('0')
else:
    print(y - x + 1)
