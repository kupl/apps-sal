a, b = list(map(str, input().split()))

if a == 'H':
    if b == 'H':
        print('H')
    else:
        print('D')
else:
    if b == 'H':
        print('D')
    else:
        print('H')
