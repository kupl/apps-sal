import sys
def I():
    return sys.stdin.readline().rstrip()

q = int( I() )
for _ in range( q ):
    n, k = list(map( int, I().split() ))
    l = I()
    r = []
    o = 0
    for i in l:
        if i == '1':
            o += 1
        else:
            t = max( 0, o - k )
            r.extend( [ '1' ] * t )
            o -= t
            k -= o
            r.append( '0' )
    r.extend( [ '1' ] * o )
    print( "".join( r ) )

