import math
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    theta = 2 * n
    y = 1 / math.sin(math.radians(360 / 4 / n)) / 2
    p = [(0, y)]
    
    rot45 =  [math.cos(math.radians(45)), -math.sin(math.radians(45))], [math.sin(math.radians(45)), math.cos(math.radians(45))]
    tmp = p[-1]
    x = rot45[0][0] * tmp[0] + rot45[0][1] * tmp[1]
    y = rot45[1][0] * tmp[0] + rot45[1][1] * tmp[1]
    p[0] = (x, y)
    the = 360 / (2 * n) 
    rot = [math.cos(math.radians(the)), -math.sin(math.radians(the))], [math.sin(math.radians(the)), math.cos(math.radians(the))]
    max_x = 0
    max_y = 0
    for i in range(2 * n - 1):
        tmp = p[-1]
        x = rot[0][0] * tmp[0] + rot[0][1] * tmp[1]
        y = rot[1][0] * tmp[0] + rot[1][1] * tmp[1]
        max_x = max(abs(x), max_x)
        max_y = max(abs(y), max_y)
        p.append((x, y))
    print(2 * max_x)

