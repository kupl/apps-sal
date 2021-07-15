N = int( input() )
A = list( map( int, input().split() ) )
dp = [ [ - int( 1e9 ) for i in range( 2 ) ] for j in range( N + 1 ) ]
dp[ 0 ][ 0 ] = 0
for i in range( N ):
  for j in range( 2 ):
    if abs( A[ i ] ) & 1:
      dp[ i + 1 ][ j ] = max( dp[ i ][ j ], dp[ i ][ j ^ 1 ] + A[ i ] )
    else:
      dp[ i + 1 ][ j ] = max( dp[ i ][ j ], dp[ i ][ j ] + A[ i ] )
print( dp[ N ][ 1 ] )

