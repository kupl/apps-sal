from sys import stdin
(a, b) = map(int, stdin.readline().split())
aa = bb = ab = 0
for x in (1, 2, 3, 4, 5, 6):
    if abs(x - a) < abs(x - b):
        aa += 1
    elif abs(x - a) > abs(x - b):
        bb += 1
    else:
        ab += 1
print('{} {} {}'.format(aa, ab, bb))
