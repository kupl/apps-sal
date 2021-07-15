n = int( input() )
a = int( input() )
b = int( input() )

#print( n, a, b )

MAXVAL = 10000000

for x in range( MAXVAL ):
    y = ( n - x * a ) // b

    if y < 0:
        break

    if a * x + y * b == n:
        print( "YES" )
        print( x, y )
        return

print( "NO" )
