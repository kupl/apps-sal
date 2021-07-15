n = int(input())
l = list( map( int, input().split() ) )
l = [ (v, i) for i, v in enumerate( l ) ]
l.sort()
l.reverse()
s, x = 0, 0
for v, i in l:
    s += v * x + 1
    x += 1

print( s )
for v, i in l:
    print( i + 1 )

