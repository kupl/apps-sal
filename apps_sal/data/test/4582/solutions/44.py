a,b = (input().split())

if (a == 'H' and b == 'H') or (a == 'D' and b == 'D'):
    print('H')

elif (a == 'H' and b == 'D') or (a == 'D' and b == 'H'):
    print('D')
