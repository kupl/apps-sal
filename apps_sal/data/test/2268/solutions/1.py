A = list("abcdefghijklmnopqrstuvwxyz")
n, m = map( int, input().split() )
name = input()

for i in range( m ) :
    s = input()
    x, y = s[0], s[2]

    x_index = A.index( x )
    y_index = A.index( y )

    A[x_index], A[y_index] = A[y_index], A[x_index]

for c in name :
    index = ord( c ) - ord( 'a' )
    print( A[index], end='')

