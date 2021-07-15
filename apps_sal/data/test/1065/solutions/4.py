n, k, m, d = map( int, input().split( ' ' ) )

ans = 0
hand = 0

for i in range( d ):
	koita = hand + 1
	val = min( n // koita, m )
	ans = max( ans, val * ( i + 1 ) )
	hand += k

print( ans )
