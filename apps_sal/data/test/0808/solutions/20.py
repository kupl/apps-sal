s = input()
if not '.' in s:
    s = s + '.'
(a, b) = s.strip('0').split('.')
if not a:
    newb = b.strip('0')
    (poc, l, r) = (len(newb) - len(b) - 1, newb[0], newb[1:])
else:
    (poc, l, r) = (len(a) - 1, a[0], (a[1:] + b).rstrip('0'))
if l:
    print(l, end='')
else:
    print(0, end='')
if r:
    print('.' + r, end='')
if poc:
    print('E%d' % poc, end='')
