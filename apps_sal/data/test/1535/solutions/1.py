from fractions import gcd
n, x, y = list(map(int, input().split()))
L = {}
for i in range(n):
    a, b = list(map(int, input().split()))
    dy = y - b
    dx = x - a
    if(dx < 0):
        dy = -dy
        dx = -dx
    g = gcd(dy, dx)
    dy //= g
    dx //= g
    L[(dy, dx)] = 1
print(len(L))
