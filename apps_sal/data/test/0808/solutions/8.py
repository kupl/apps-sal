import re

a = input()
if not '.' in a: a += '.'

a, b = a.strip('0').split('.')

st = 0
if len(a) > 1:
    st = len(a) - 1
    b = (a[1:] + b).rstrip('0')
    a = a[0]
elif len(a) == 0:
    r = b.strip('0')
    st = - (len(b) - len(r) + 1)
    a = r[0]
    b = r[1:]

if a: print(a, end='')
if b: print('.' + b, end='')
if st: print('E' + str(st))
