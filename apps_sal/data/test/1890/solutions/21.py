MOD = int( 1e9 + 7 )

A = input()
K = int( input() )

ans = 0
q = 1
for i in range( len( A ) ):
  if A[ i ] == '0' or A[ i ] == '5':
    ans = ( ans + q ) % MOD
  q = q * 2 % MOD

print( ans * ( pow( 2, K * len( A ), MOD ) - 1 ) * pow( pow( 2, len( A ), MOD ) - 1, MOD - 2, MOD ) % MOD )

