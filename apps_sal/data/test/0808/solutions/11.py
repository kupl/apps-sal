s = input()
if not '.' in s:
    s += '.'
a, b = s.strip('0').split('.')
if len(a) > 0:
    b = (a[1:] + b).rstrip('0')
    le = len(a) - 1
    a = a[0]
else:
    le = len(b.strip('0')) - len(b) - 1
    b = b.strip('0').rstrip('0')
    a = b[0]
    b = b[1:]

print(a, end='')
if len(b):
    print('.' + b, end='')
if le:
    print('E' + str(le))
