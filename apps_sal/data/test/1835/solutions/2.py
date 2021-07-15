import sys
def I():
    return sys.stdin.readline().rstrip()

q = int( I() )
for _ in range( q ):
    n = int( I() )
    one, zero, odd = 0, 0, 0
    for _ in range( n ):
        s = I()
        odd += len( s ) & 1
        for c in s:
            if c == '0':
                zero += 1
            else:
                one += 1
    if ( one & 1 ) == 1 and ( zero & 1 ) == 1 and odd == 0:
        n -= 1
    print( n )

