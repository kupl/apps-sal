import sys
import math

r1, c1, r2, c2 = [int(x) for x in (sys.stdin.readline()).split()]

res = []
if(r1 == r2 and c1 == c2):
    print("0 0 0")
    return

if(r1 == r2 or c1 == c2):
    res.append("1")
else:
    res.append("2")

f1 = ((r1 + c1) % 2 == 0)
f2 = ((r2 + c2) % 2 == 0)

if(f1 != f2):
    res.append("0")
elif(math.fabs(r1 - r2) == math.fabs(c1 - c2)):
    res.append("1")
else:
    res.append("2")

res.append(str(int(max(math.fabs(r1 - r2), math.fabs(c1 - c2)))))

print(" ".join(res))
