import math
a, b, x = map(int, input().split())
c = x/a**2  # c : height of water

if c >= b/2:
    tanth = 2*(b-c)/a
    deg = math.atan(tanth)*180/math.pi
else:
    tanth = b**2/(2*a*c)
    deg = math.atan(tanth)*180/math.pi

print(deg)
