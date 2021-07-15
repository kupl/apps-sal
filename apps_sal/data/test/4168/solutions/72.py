n = int( input() )

if n == 0:
    print('0')
else:
    sum = 0
    i = 0
    S = []
    while n != 0:

        x = n % (2 ** (i+1))
        if x != 0:
            S.append('1')

            n -= (-2) ** i

        else:
            S.append('0')
        i += 1
    
    S = S[::-1]
    strS = ''.join(S)
    print(strS)

