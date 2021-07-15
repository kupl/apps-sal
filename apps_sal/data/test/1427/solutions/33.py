import math
from functools import reduce
     
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
     
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
      
N = int(input())
A = list(map(int,input().split()))
ans = 0
     
lcm = lcm_list(A)
     
for i in range(N):
    ans += lcm//A[i]
     
print(ans%1000000007)
