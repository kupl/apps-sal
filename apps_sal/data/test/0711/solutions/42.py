import math
def fac(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
def com(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, list(range(n, n - r, -1)))
    under = reduce(mul, list(range(1,r + 1)))
    return over // under
ans = 1
a,b = list(map(int,input().split()))
l = fac(b)
for i in l:
  ans *= cmb(i[1]+a-1,a-1)
  ans = ans % (10**9 + 7)
if b == 1:
  print((1))
else:
  print(ans)

  

