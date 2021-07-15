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

def leaf(x,y):
    m = (y-x)//2
    for aa,bb in pairs:
        if aa<x<bb or aa<y<bb or (x<=aa<bb<=y and bb-aa!=m):
            return False
    for i in range(m):
        if bl[x+i] or al[x+m+i] or \
           (al[x+i] and not pal[x+i] and bl[x+m+i]):
            return False
    return True

n = inn()
pal = [False]*(2*n)
al = [False]*(2*n)
bl = [False]*(2*n)
pairs = []
for i in range(n):
    a,b = inm()
    a -= 1
    b -= 1
    if a>=0 and (al[a] or bl[a]) or b>=0 and (al[b] or bl[b]):
        print('No')
        return
    if a>=0:
        al[a] = True
    if b>=0:
        bl[b] = True
    if a>=0 and b>=0:
        if a>=b:
            print('No')
            return
        pairs.append((a,b))
        pal[a] = True

dp = [False]*(2*n+1)
dp[0] = True
for i in range(1,n+1):
    for j in range(i):
        if dp[j] and leaf(2*j,2*i):
            dp[i] = True
            break
print('Yes' if dp[n] else 'No')

