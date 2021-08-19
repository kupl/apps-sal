x = int(input())
K = {}
K[0] = 'O-|-OOOO'
K[1] = 'O-|O-OOO'
K[2] = 'O-|OO-OO'
K[3] = 'O-|OOO-O'
K[4] = 'O-|OOOO-'
K[5] = '-O|-OOOO'
K[6] = '-O|O-OOO'
K[7] = '-O|OO-OO'
K[8] = '-O|OOO-O'
K[9] = '-O|OOOO-'
if x == 0:
    print('O-|-OOOO')
else:
    while x != 0:
        d = x % 10
        print(K[d])
        x //= 10
