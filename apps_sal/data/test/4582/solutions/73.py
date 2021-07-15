# 056_a
a, b = input().split()
if (a == 'H' or a == 'D') and (b == 'H' or b == 'D'):
    if a == 'H':
        if b=='H':
            print('H')
        else:
            print('D')
    if a == 'D':
        if b=='H':
            print('D')
        else:
            print('H')

