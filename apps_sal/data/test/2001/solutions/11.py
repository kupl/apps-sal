from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
import sys
import math
MAX = sys.maxsize
MOD = 10**9+7
MAXN = 10**6+10
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def mhd(a,b,x,y):
    return abs(a-x)+abs(b-y)

def numIN():
    return(map(int,sys.stdin.readline().strip().split()))

def charIN():
    return(sys.stdin.readline().strip().split())

def maxSubArraySum(a,size): 
      
    max_so_far = 0
    max_ending_here = 0
      
    for i in range(size): 
        max_ending_here = max_ending_here + a[i] 
        if max_ending_here < 0: 
            max_ending_here = 0 
        elif (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
              
    return max_so_far

def isPer(n):
	return((math.floor(n**0.5))==(math.ceil(n**0.5)))

def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x

n,q = numIN()
l = [int(i) for i in input()]
pre = []
s = 0
for i in l:
	s+=i
	pre.append(s)
for i in range(q):
	l,r = numIN()
	l-=1
	r-=1
	if l!=0:
		one = pre[r]-pre[l-1]
		zero = r-l+1-one
		x = pow(2,one,MOD)-1
		y = pow(2,zero,MOD)
		ans = x*y
		ans%=MOD
		print(ans)
	else:
		one = pre[r]
		zero = r-l+1-one
		x = pow(2,one,MOD)-1
		y = pow(2,zero,MOD)
		ans = x*y
		ans%=MOD
		print(ans)
