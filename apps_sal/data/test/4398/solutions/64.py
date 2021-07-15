n = int( input() )
s, t = input().split()

u = ""
for i in range( n ):
    u = u + s[ i ] + t[ i ]

print( u )
