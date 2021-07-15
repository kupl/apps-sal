N = int( input() )
A = [ input() for i in range( N ) ]
for i in range( N - 1, 0, -1 ):
  if A[ i - 1 ] > A[ i ]:
    ptr = 0
    while ptr < len( A[ i ] ) and A[ i - 1 ][ ptr ] == A[ i ][ ptr ]:
      ptr += 1
    A[ i - 1 ] = A[ i - 1 ][ : ptr ]
print( '\n'.join( A ) )

