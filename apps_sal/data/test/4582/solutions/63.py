a, b = list(map(str, input().split()))
if a == 'H' and b == 'H':
    print('H')
elif a == 'H' and b == 'D':
    print('D')
elif a == 'D' and b == 'H':
    print('D')
else:
    print('H')
