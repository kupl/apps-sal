n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
maxcount = 0
if a1 - b2 > 0 and b2 != 0:
    maxcount += (b2)
elif b2 == 0:
    maxcount += 0
else:
    maxcount += a1
if a2 - b3 > 0 and b3 != 0:
    maxcount += (b3)
elif b3 == 0:
    maxcount += 0
else:
    maxcount += a2
if a3 - b1 > 0 and b1 != 0:
    maxcount += (b1)
elif b1 == 0:
    maxcount += 0
else:
    maxcount += a3
mincount = 0
if a1 > b1 + b3:
    mincount += (a1 - b1 - b3)
if a2 > b1 + b2:
    mincount += (a2 - b1 - b2)
if a3 > b2 + b3:
    mincount += (a3 - b2 - b3)
print(mincount, maxcount)
