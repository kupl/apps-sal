import math
nm = input().split()
nm[0] = int(nm[0])
nm[1] = int(nm[1])
pwords = []
ewords = []
for x in range(0, nm[0]):
    pwords.append(input())
for x in range(0, nm[1]):
    ewords.append(input())
nump = 0
nume = 0
common = 0
for x in range(0, nm[0]):
    if pwords[x] in ewords:
        common = common + 1
nump = nm[0] - common + math.ceil(common / 2)
nume = nm[1] - common + math.floor(common / 2)
if nump > nume:
    print('YES')
else:
    print('NO')
