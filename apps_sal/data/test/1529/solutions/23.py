n = int(input())
for i in range(n):
    t = input()
    a = b = len(t) > 4
    a = a and t[:5] == 'miao.'
    b = b and t[-5:] == 'lala.'
    if a:
        if b: print('OMG>.< I don\'t know!')
        else: print('Rainbow\'s')
    else:
        if b: print('Freda\'s')
        else: print('OMG>.< I don\'t know!')
