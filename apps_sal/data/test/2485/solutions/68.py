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

h,w,m = inm()
ha = [0]*h
wa = [0]*w
q = {}
for i in range(m):
    hh,ww = inm()
    hh -= 1
    ww -= 1
    q[(hh,ww)] = 1
    ha[hh] += 1
    wa[ww] += 1
mh = max(ha)
mw = max(wa)
a = [i for i in range(h) if ha[i]==mh]
b = [i for i in range(w) if wa[i]==mw]
for i in a:
    for j in b:
        if (i,j) not in q:
            print(mh+mw)
            return
print(mh+mw-1)

