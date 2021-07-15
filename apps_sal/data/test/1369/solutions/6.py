import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print((' '.join(map(str, l))))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

n = n_in()
xy = [l_in() for _ in range(n)]

left = 0
right = 2000

from itertools import combinations
import math
def check(r):
    allprox = True
    for (x1,y1),(x2,y2) in combinations(xy, 2):
        dx = x1-x2
        dy = y1-y2

        d2 = dx*dx+dy*dy

        if d2 < 10**-16:
            continue

        allprox = False
        
        if d2/4 > r*r:
            continue

        h = math.sqrt(r*r-d2/4)
        d = math.sqrt(d2)

    
        px,py= (x1+x2)/2, (y1+y2)/2

        qx,qy = px-dy/d*h, py+dx/d*h
        if all((qx-x3)*(qx-x3) + (qy-y3)*(qy-y3) <= r*r for x3,y3 in xy if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3)):
            return True
        
        qx,qy = px+dy/d*h, py-dx/d*h
        if all((qx-x3)*(qx-x3) + (qy-y3)*(qy-y3) <= r*r for x3,y3 in xy if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3)):
            return True
    else:
        return allprox

while right-left > 10**-10:
    mid = (left+right)/2
    if check(mid):
        right = mid
    else:
        left = mid

print(((left+right)/2))
    

