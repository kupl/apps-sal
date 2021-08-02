import sys
n, a, x, b, y = list(map(int, input().split()))
z1 = a
z2 = b
while True:
    if z1 == z2:
        print("YES")
        return
    if z1 == x or z2 == y:
        print("NO")
        return
    z1 = (z1 % n) + 1
    if z2 == 1:
        z2 = n
    else:
        z2 -= 1
