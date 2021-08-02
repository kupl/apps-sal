n = input()
while n:
    k = int(n) % 10
    n = n[:len(n) - 1]
    if k > 4:
        print('-O|', end='')
        if (k - 5) % 4 == 0 and k != 5:
            print('O' * 4, '-', sep='')
            if k - 5 < 4:
                print('-', 'O' * (4 - k % 5), sep='')
        elif k == 5:
            print('-OOOO')
        else:
            print('O' * ((k - 5) % 4), end='')
            if k - 5 < 4:
                print('-', 'O' * (4 - k % 5), sep='')
    else:
        print('O-|', 'O' * k, '-', 'O' * (4 - k), sep='')
