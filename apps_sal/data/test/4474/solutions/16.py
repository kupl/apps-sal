import sys
def I():
    return sys.stdin.readline().rstrip()

N = 39
p = [ 3 ** i for i in range( N ) ]

q = int( I() )
for _ in range( q ):
    n = int( I() )
    a = [ 0 ] * N
    for i in range( N - 1, -1, -1 ):
        d = n // p[ i ]
        n -= d * p[ i ]
        if d == 2:
            j = i + 1
            while a[ j ]:
                a[ j ] = 0
                j += 1
            a[ j ] = 1
            break
        a[ i ] = d
    n = 0
    for i in range( N ):
        if a[ i ]:
            n += p[ i ]
    print( n )

