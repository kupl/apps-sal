import sys
input = sys.stdin.readline
l = list(map(int, input().split()))
recA = l[:2]
recB = l[2:]
areaA = int(recA[0]) * int(recA[-1])
areaB = int(recB[0]) * int(recB[-1])
if areaA > areaB:
    print(areaA)
elif areaB > areaA:
    print(areaB)
elif areaB == areaA:
    print(areaB)
