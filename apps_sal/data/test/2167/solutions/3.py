import sys
import math
n = int(sys.stdin.readline())
an = [int(x) for x in sys.stdin.readline().split()]
vsum = sum(an)
if vsum % n == 0:
    print(int(n))
else:
    print(int(n - 1))
