# https://codeforces.com/problemset/problem/912/D
import heapq
from heapq import heappush as push
from heapq import heappop  as pop

base = 100009
Q=[]
used={}
ans=0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def f(x, y):
    x1, x2 = min(x, r-1),   max(0, x-n+r)
    y1, y2 = min(y, r-1),   max(0, y-m+r)
    
    return -(x1-x2+1)*(y1-y2+1)
    
def cal(i, j):
    return i*base+j

def get(ind):
    return ind//base, ind%base

def is_ok(x, y, x_, y_):
    if x+x_>=0 and x+x_<n and y+y_>=0 and y+y_<m:
        return True
    return False
   
n, m, r, k = map(int, input().split())    
x0, y0 = n//2, m//2 
Q=[(f(x0, y0), cal(x0, y0))]

while k > 0:
    val, ind = pop(Q)
    
    if ind in used:
        continue
        
    x, y = get(ind)
    used[ind]=True
    val  = -val
    #print((x, y), val)
    ans += val
    for x_, y_ in zip(dx, dy):
        if is_ok(x, y, x_, y_):
            push(Q, (f(x+x_, y+y_), cal(x+x_, y+y_)))
    k-=1
    
print(ans/((n-r+1)*(m-r+1)))    
