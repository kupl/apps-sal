(a, b) = input().split()
if a == 'H':
    if b == 'H':
        print('H')
    elif b == 'D':
        print('D')
elif a == 'D':
    if b == 'H':
        print('D')
    elif b == 'D':
        print('H')
