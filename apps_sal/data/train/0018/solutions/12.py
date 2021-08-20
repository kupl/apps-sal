import math
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    theta = 2 * n
    print(1 / math.tan(math.radians(360 / 4 / n)))
