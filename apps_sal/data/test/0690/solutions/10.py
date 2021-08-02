n = [int(x) for x in input()]
n.reverse()
for i in range(len(n)):
    if n[i] >= 5:
        print('-O|', end='')
        q = n[i] - 5
    else:
        print('O-|', end='')
        q = n[i]

    if q == 0:
        print('-OOOO')
    if q == 1:
        print('O-OOO')
    if q == 2:
        print('OO-OO')
    if q == 3:
        print('OOO-O')
    if q == 4:
        print('OOOO-')
