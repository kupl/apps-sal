#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

import heapq
n,k,q = inm()
a = inl()
mn = BIG
for i in range(n):
    #ddprint(f"{i=}")
    lo = a[i]
    gr = []
    bg = -1
    for j in range(n):
        #ddprint(f"  {j=} {lo=} {bg=} {a[j]=}")
        if lo<=a[j]:
            if bg<0:
                bg = j
        else:
            if bg>=0:
                if j>=bg+k:
                    gr.append((bg,j))
                bg = -1
    if bg>=0 and n>=bg+k:
        gr.append((bg,n))
    ddprint(gr)
    h = []
    for bg,ed in gr:
        b = a[bg:ed]
        b.sort()
        #ddprint(f"{bg=} {ed=} {b=}")
        for j in range(len(b)-k+1):
            heapq.heappush(h,b[j])
    ddprint(h)
    if len(h)<q:
        continue
    mn0 = BIG
    mx = -1
    for j in range(q):
        v = heapq.heappop(h)
        mx = max(mx,v)
        mn0 = min(mn0,v)
    mn = min(mn,mx-mn0)
print(mn)

