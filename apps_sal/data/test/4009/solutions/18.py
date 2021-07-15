n, x, y = map( int, input().split() )

s = input()

ans = 0

for i in range( x ):
    if s[ -(i + 1) ] != ( '1' if i == y else '0' ) :
        ans += 1

print( ans )
