s = input()
if '.' not in s:
    s += '.'
s = s.strip('0')
(a, b) = s.split('.')
if len(a):
    b = a[1:] + b
    b = b.rstrip('0')
    l = len(a) - 1
    a = a[0]
else:
    l = len(b.strip('0')) - len(b) - 1
    b = b.strip('0').rstrip('0')
    a = b[0]
    b = b[1:]
print(a, end='')
if len(b):
    print('.' + b, end='')
if l:
    print('E' + str(l))
