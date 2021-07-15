from sys import stdin
input = stdin.readline
from fractions import gcd
 
mod = 10**9+7
 
n = int(input())
a = list(map(int,input().split()))
d = 1
for i in range(n):
  d *= a[i] // gcd(a[i],d)
ans = 0
for i in range(n):
  ans += d//a[i]
 
print(ans%mod)
