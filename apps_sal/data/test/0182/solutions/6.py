a, b, c = tuple(map(int, input().split()))
x, y, z = tuple(map(int, input().split()))

have = 0
need = 0

if a > x:
    have += (a - x) // 2
else:
    need += x - a

if b > y:
    have += (b - y) // 2
else:
    need += y - b
    
if c > z:
    have += (c - z) // 2
else:
    need += z - c

if need > have:
    print('No')
else:
    print('Yes')
