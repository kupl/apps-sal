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

def f(n,x):
    nonlocal h
    if x>2**(n+2)-3:
        x = 2**(n+2)-3
    if (n,x) in h:
        return h[(n,x)]
    ret = -1
    if n==0:
        ret = x
    elif x<=1:
        ret = 0
    elif x<=2**(n+1)-2:
        ret = f(n-1,x-1)
    elif x==2**(n+1)-1:
        ret = 2**n
    elif x<=2**(n+2)-4:
        ret = 2**n+f(n-1,x-2**(n+1)+1)
    else:
        ret = 2**(n+1)-1
    h[(n,x)] = ret
    return ret

n,x = inm()
h = {}
print(f(n,x))

