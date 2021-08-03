def read(): return map(int, input().split())


a, b, c = read()
x, y, z = read()
m, n, k = x - a, y - b, z - c
p = 0
q = 0
if m > 0:
    p += m
else:
    q += (-m) // 2
if k > 0:
    p += k
else:
    q += (-k) // 2
if n > 0:
    p += n
else:
    q += (-n) // 2

print('Yes' if q >= p else 'No')
