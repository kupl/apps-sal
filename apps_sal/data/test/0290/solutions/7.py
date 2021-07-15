n = int( input() )

a = 0
b = 0

while a * b < n:
    if a == b:
        a += 1
    else:
        b += 1

print( a + b )

