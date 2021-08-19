IN = input().split()

day = int(IN[0])
if IN[2] == 'week':
    if day == 5 or day == 6:
        print('53')
    else:
        print('52')
else:  # month
    if day < 30:
        print('12')
    elif day < 31:
        print('11')
    else:
        print('7')
