N, K = map( int, input().split() )
mod = 10 ** 9 + 7
Cnt = [ 0 ] * ( K + 1 )

for i in range( K, 0, -1 ):
  elem_cnt = K // i
  i_s_cnt = pow( elem_cnt, N, mod)
  for j in range( 2, elem_cnt + 1 ):
    i_s_cnt -= Cnt[ i * j ]
  Cnt[ i ] = i_s_cnt

cnt = 0
for i , c in enumerate( Cnt ):
  cnt += i * c
  cnt = cnt % mod 

print( cnt )
