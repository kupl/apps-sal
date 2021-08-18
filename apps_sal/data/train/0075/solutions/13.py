from math import sin, tan, cos, pi

for t in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(1 / tan(pi / (2 * n)))
    else:
        print(1 / sin(pi / (2 * n)) * cos(pi / (4 * n)))
