(a, b) = input().split('=')
if abs(len(a) - 1 - len(b)) not in [0, 2]:
    print('Impossible')
elif len(a) - 1 == len(b):
    print(a + '=' + b)
elif len(a) - 1 < len(b):
    print('|' + a + '=' + b[:-1])
elif a.find('+') > 1:
    print(a[1:] + '=' + b + '|')
else:
    print(a[:-1] + '=' + b + '|')
