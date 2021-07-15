import math
import collections
import sys

input = sys.stdin.readline
def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]

n,m=MI()
A=LI()
def num2(x):
    ans=0
    while x%2==0:
        x=x//2
        ans+=1
    return ans
mod=2**(num2(A[0]))
for i in range(1,n):
    if A[i]%mod!=0:
        print((0))
        return
    if A[i]%mod==0 and (A[i]//mod)%2==0:
        print((0))
        return
#print(A)
for i in range(n):
    A[i]//=2
#print(A)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

L=A[0]   
for i in range(1,n):
    L=lcm(L,A[i])
#print(L)
if L>m:
    an=0
else:
    an=int(((m/L)-1)/2)+1
print(an)

