from sys import stdin
import re
import math

def readInt(count=1):
    m = re.match('\s*' + ('([+-]?\d+)\s*' * count), stdin.readline())
    if m is not None:
        ret = []
        for i in range(1, m.lastindex + 1):
            ret.append(int(m.group(i)))
        return ret
    return None

x, y, l, r = readInt(4)

max = 0
unhappyYears = [l-1]
xa = 1
while xa <= r:
    yb = 1
    while True:
        val = xa + yb
        if val > r:
            break
        if val >= l and val not in unhappyYears:
            unhappyYears.append(val)
        yb *= y
    xa *= x
unhappyYears.sort()
unhappyYears.append(r+1)

for i in range(len(unhappyYears)-1):
    cur = unhappyYears[i+1] - unhappyYears[i] - 1
    if cur > max:
        max = cur
print(max)
