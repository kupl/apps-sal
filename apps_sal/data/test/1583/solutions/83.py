
from math import atan, degrees

a, b, x = map(int, input().split())
volume = a * a * b

if x * 2 >= volume:
    h = 2 * b - 2 * x / (a * a)
    print(degrees(atan(h / a)))
else:
    h = 2 * x / (a * b)
    print(degrees(atan(b / h)))
