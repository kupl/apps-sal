from collections import Counter as C
for TT in range(1, int(input()) + 1):
    n = int(input())   
    c = C(map(lambda x: int(x) % 3, input().split()))
    x, y, z = c.get(0, 0), c.get(1, 0), c.get(2, 0) 
    d = min(y, z)
    y -= d
    z -= d
    x += d
    y //= 3
    z //= 3
    print(x + y + z)
