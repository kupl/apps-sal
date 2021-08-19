import sys
import math
import fractions
f = sys.stdin
line_ = list(map(int, f.readline().split()))
line = []
for it in line_:
    line.append(it)
x = int(line[0])
y = int(line[1])
a = int(line[2])
b = int(line[3])
xy = x * y / fractions.gcd(x, y)
ans = b // xy - (a - 1) // xy
print(int(ans))
