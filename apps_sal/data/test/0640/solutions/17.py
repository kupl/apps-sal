from sys import stdin

a,b = map(int,stdin.readline().split())

aa = bb = ab = 0
for x in range(1,7):
    if abs(x-a) < abs(x-b):
        aa += 1
    elif abs(x-a) > abs(x-b):
        bb += 1
    else:
        ab += 1

print("{} {} {}".format(aa,ab,bb))
