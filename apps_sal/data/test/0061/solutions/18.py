n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
l, k = list(map(int, input().split()))
b = list(map(int, input().split()))
c1 = 0
c2 = 0
for i in range(n - 1, -1, -1):
    c1 += m ** (n - 1 - i) * a[i]
for t in range(l - 1, -1, -1):
    c2 += k ** (l - 1 - t) * b[t]
if c1 == c2:
    print('=')
elif c1 < c2:
    print('<')
else:
    print('>')

