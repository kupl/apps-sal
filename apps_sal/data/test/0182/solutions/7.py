a, b, c = list(map(int, input().split()))
x, y, z = list(map(int, input().split()))
if a >= x:
    a -= x
    x = 0
else:
    x -= a
    a = 0
    

if b >=y:
    b -= y
    y = 0
else:
    y -= b
    b = 0

if c >= z:
    c -= z
    z = 0
else:
    z -= c
    c= 0
    
if a // 2 + b // 2 + c // 2 >= x + y + z:
    print('Yes')
else:
    print('No')

