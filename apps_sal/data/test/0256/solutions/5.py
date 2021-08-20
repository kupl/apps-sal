import sys


def read():
    return list(map(int, sys.stdin.readline().split()))


(a0, d0) = read()
(a1, d1) = read()
(a2, d2) = read()
(a3, d3) = read()
w02 = a0 > d3 and d1 > a2
w03 = a0 > d2 and d1 > a3
w12 = a1 > d3 and d0 > a2
w13 = a1 > d2 and d0 > a3
w20 = a2 > d1 and d3 > a0
w21 = a2 > d0 and d3 > a1
w30 = a3 > d1 and d2 > a0
w31 = a3 > d0 and d2 > a1
if w02 and w03 or (w12 and w13):
    print('Team 1')
elif (w20 or w30) and (w21 or w31):
    print('Team 2')
else:
    print('Draw')
