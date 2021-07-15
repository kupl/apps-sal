#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

n,a,b = inm()
flip = False
if a<b:
    a,b = b,a
    flip = True
if a*a<n or n<a or a+b-1>n or a*b<n:
    print(-1)
    return
d = [0]*(a+1)
m = n
for i in range(1,a+1):
    d[i] = min(b,m-(a-i))
    m -= d[i]
t = []
x = 1
for z in d[1:]:
    y = list(range(x,x+z))
    x += z
    y.reverse()
    t.extend(y)
if flip:
    t.reverse()
print(' '.join([str(x) for x in t]))

