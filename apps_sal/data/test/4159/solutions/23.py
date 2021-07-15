a, b, k = map( int, input().split() )

if a + b < k:
    print( "0 0" )
elif a < k:
    print( "0 " + str( a + b - k ) )
else:
    print( str( a - k ) + " " + str( b ) )
