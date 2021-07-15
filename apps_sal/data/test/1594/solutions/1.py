#CF302B
r = input().split(' ')
n = int( r[ 0 ] )
m = int( r[ 1 ] )
s = []

for i in range( 0 , n ):
    r = input().split(' ')
    s.append( int( r[ 0 ] ) * int( r[ 1 ] ) )
    if i > 0:
        s[ i ] += s[ i - 1 ]

r = input().split(' ')
ct = 0
for i in range( 0 , m ):
    v = int( r[ i ] )
    while s[ ct ] < v :
        ct += 1
    print( ct + 1 )

