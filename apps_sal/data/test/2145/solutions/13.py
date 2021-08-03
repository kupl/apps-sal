import sys
import math
T = int(sys.stdin.readline())
for i in range(T):
    xy = sys.stdin.readline().split(" ")
    start = int(xy[0])
    target = int(xy[1])
    if start >= target or start >= 4 or (start == 2 and target == 3):
        print("YES")
    else:
        print("NO")
