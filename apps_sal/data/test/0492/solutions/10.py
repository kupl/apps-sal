import math


def ria():
    return [int(i) for i in input().split()]


a, b = input().split()
n = ria()[0]
possible = []

st = "^>v<"
if (st[(st.find(a) + n) % 4]) == b:
    possible.append('cw')

if (st[(st.find(a) - n) % 4]) == b:
    possible.append('ccw')
if possible.__len__() > 1:
    print('undefined')
else:
    print(possible[0])
