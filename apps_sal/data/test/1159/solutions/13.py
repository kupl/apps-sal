def isp( n ):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int( input() )
e = [ [ i + 1, ( i + 1 ) % n + 1 ] for i in range( n ) ]
i = 0
while not isp( len( e ) ):
    e.append( [ i + 1, (i + n//2) % n + 1 ] )
    i += 1

print( len( e ) )
for ed in e:
    print( *sorted(ed) )

