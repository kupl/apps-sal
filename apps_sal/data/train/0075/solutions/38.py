import math
from sys import stdin, stdout
for _ in range(int(stdin.readline().strip())):
    n = 2*int(stdin.readline().strip())
    ans = 1/((math.sin(math.radians(90/n))))
    print("{0:.9f}".format(ans/2))
