import string

s = input()

ans = len( s ) // 2 + 1

for a in list( string.ascii_lowercase ):
    last = -1
    l = 0
    for i , c in enumerate( list( s ) ):
        if a == c:
            l = max( l, i - last )
            last = i
    l = max( l , len( s ) - last )
    ans = min( ans, l )

print( ans )

