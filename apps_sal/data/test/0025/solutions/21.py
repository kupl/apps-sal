N, K = map( int, input().split() )
if K > N * N:
  exit( print( -1 ) )
G = [ [ 0 for i in range( N ) ] for j in range( N ) ]
for i in range( N ):
  if K == 0: break
  G[ i ][ i ] = 1
  K -= 1
  for j in range( i + 1, N ):
    if K <= 1: break
    G[ i ][ j ], G[ j ][ i ] = 1, 1
    K -= 2
for i in range( N ):
  print( ' '.join( str( v ) for v in G[ i ] ) )

