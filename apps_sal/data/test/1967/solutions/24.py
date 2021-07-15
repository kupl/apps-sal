w, h = map( int, input( ).split( ) )
stgs = [ ]

for i in range( h ):
    stgs.append( input( )  )

m = [0] * h
for i in range(h):
    m[i] = [0] * w

for i in range( h ):
    for j in range( w ):
        m[ i ][ j ] = stgs[ i ][ j ]

for i in range( h ):
    m[ i ].reverse( )

sk = 1
st = ""

for i in range( w - 1, -1, -1 ):
    for j in range( h ):
        st += m[ j ][ i ] + m[ j ][ i ]
    print( st, st, sep = '\n' )
    st = ''

