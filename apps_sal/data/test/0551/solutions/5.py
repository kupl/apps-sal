def f(m, c1, c2, l, n):
    fl = True
    for i in range(n):
        if l[i] - (m1 * i + m1) != c1 and l[i] - (m1 * i + m1) != c2:
            fl = False
            break
    return fl and c1 != c2


n = int(input())
l = list(map(int, input().split()))
m1 = l[1] - l[0]
c1 = l[0] - m1
c2 = c1
for i in range(n):
    if l[i] - m1 * (i + 1) != c1:
        c2 = l[i] - m1 * (i + 1)
f1 = f(m1, c1, c2, l, n)
m1 = l[1] - l[0]
c1 = l[0] - m1
c2 = l[2] - m1 * 3
f2 = f(m1, c1, c2, l, n)
m1 = (l[2] - l[0]) / 2
c1 = l[0] - m1
c2 = l[1] - m1 * 2
f3 = f(m1, c1, c2, l, n)
m1 = l[2] - l[1]
c1 = l[0] - m1
c2 = l[1] - m1 * 2
f4 = f(m1, c1, c2, l, n)
if f1 or f2 or f3 or f4:
    print('Yes')
else:
    print('No')
