read = lambda: map(int, input().split())
n, k = read()
b = bin(n)[2:]
bl = len(b)
k -= b.count('1')
if k < 0:
    print('No')
    return
print('Yes')
m = -2
a = {}
for _ in range(bl):
    if b[_] == '1':
        a[bl - _ - 1] = 1
        if m is -2:
            m = bl - _ - 1
while k > 0:
    if k >= a[m]:
        k -= a[m]
        a[m - 1] = a.get(m - 1, 0) + a[m] * 2
        a.pop(m)
        m -= 1
    else:
        break
m = min(a.keys())
while k > 0:
    k -= 1
    if a[m] is 1:
        a.pop(m)
    else:
        a[m] -= 1
    a[m - 1] = a.get(m - 1, 0) + 2
    m -= 1
for k in sorted(list(a.keys()), reverse=True):
    print(('%d ' % k) * a[k], end='')
