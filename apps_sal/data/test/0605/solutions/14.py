from math import *
a = list(map(int, input().split()))
m = max(3 * a[0] / 10, a[0] - a[0] / 250 * a[2])
v = max(3 * a[1] / 10, a[1] - a[1] / 250 * a[3])
if m > v:
    print('Misha')
elif m < v:
    print('Vasya')
else:
    print('Tie')
