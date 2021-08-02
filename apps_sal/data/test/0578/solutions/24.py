__author__ = 'Utena'
b1, c = input().split('e')
a, b = b1.split('.')
c = int(c)
if a == '0' and b == '0':
    print(0)
    return
if b == '0':
    b = ''
if len(b) <= c:
    print(a + b + '0' * (c - len(b)))
else:
    print(a + b[:c] + '.' + b[c:])
