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

s = ins()
n = len(s)
ans = 0
for i in range(2**(n-1)):
    z = []
    head = 0
    for j in range(n-1):
        if (i>>j)%2>0:
            z.append(int(s[head:j+1]))
            head = j+1
    z.append(int(s[head:]))
    ans += sum(z)
print(ans)

