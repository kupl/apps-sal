p, q = input().split('e')
a, b = p.split('.')
b += '0' * 150
d = int(q)
a = (a + b[:d]).lstrip('0')
b = b[d:].rstrip('0')
if not a:
    a = '0'
print(a, end='')
if b:
    print('.' + b)
else:
    print()

