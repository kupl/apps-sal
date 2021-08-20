(a, b) = list(map(str, input().split()))
if a == 'H':
    if b == 'H':
        print('H')
    else:
        print('D')
elif b == 'H':
    print('D')
else:
    print('H')
