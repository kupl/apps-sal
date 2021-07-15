import sys
from math import atan2

def get_array(): return list(map(int, sys.stdin.readline().split()))
def get_ints(): return map(int, sys.stdin.readline().split())
def input(): return sys.stdin.readline().strip('\n')


def dotp(a,b):
    return a[0]*b[0] + a[1]*b[1]

def crossp(a,b):
    return abs(a[0]*b[1]-a[1]*b[0])

n = int(input())
l = []
for i in range(n):
    x,y = get_ints()
    l.append((x,y,i+1))

l.sort(key = lambda x : atan2(x[1],x[0]))

l.append(l[0])

a = l[0][:2]
b = l[1][:2]
x = l[0][2]
y = l[1][2]

dot , cross = dotp(a,b) , crossp(a,b)
mx , my = dot , cross
for i in range(1,n+1):
    a = l[i-1][:2]
    b = l[i][:2]
    ndot , ncross = dotp(a,b) ,crossp(a,b)

    if ndot*my - ncross*mx > 0:
        x = l[i-1][2]
        y = l[i][2]
        mx = ndot
        my = ncross
print(x,y)
