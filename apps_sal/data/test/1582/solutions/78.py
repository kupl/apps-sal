##以下ググった（https://at274.hatenablog.com/entry/2020/01/24/060000）
n = int( input() )

cnt = [ [ 0 for i in range( 10 ) ] for j in range( 10 ) ]
# cnt[ i ][ j ] = 先頭がi，末尾がjである，n以下の整数の個数

for k in range( n + 1 ):
    head = int( str( k )[ 0 ] )
    foot = int( str( k )[ -1 ] )
    cnt[ head ][ foot ] += 1

ans = 0
for i in range( 1, 10 ):
    for j in range( 1, 10 ):
        ans += cnt[ i ][ j ] * cnt[ j ][ i ]

print( ans )
