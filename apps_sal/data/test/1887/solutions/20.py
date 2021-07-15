n = int( input() )
l = [ list( map( int, input().split() )), list( map( int, input().split())) ]
m = [ 0, 0 ]
for i in range(n-1, -1, -1):
    mm = [ 0, 0 ]
    for j in range(2):
        l[ j ][ i ] += m[ j^1 ]
        mm[ j ] = max( m[ j ], l[ j ][ i ] )
    m = mm

print( max( m ) )

