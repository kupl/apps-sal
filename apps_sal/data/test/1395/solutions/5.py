N = input()
M = int( input() )
cur = int( N ) % M
ans = cur
for i in range( len( N ) ):
  cur -= ( ord( N[ i ] ) - ord( '0' ) ) * pow( 10, len( N ) - 1, M ) % M
  cur = cur * 10 % M
  cur = ( cur + ord( N[ i ] ) - ord( '0' ) ) % M
  if N[ ( i + 1 ) % len( N ) ] != '0':
    ans = min( ans, cur )
print( ans )

