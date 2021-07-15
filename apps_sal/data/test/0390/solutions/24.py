from sys import stdin, stdout 
from bisect import bisect_left, bisect_right
from collections import defaultdict
import math
from fractions import Fraction as frac
from random import random
cin = stdin.readline
def cout(x):
	stdout.write(str(x)+'\n')
def var(type = int):
    return type(stdin.readline())
def readline(type = int):
    return list(map(type,stdin.readline().split()))
def readlist(type = int):
    return list(map(type,stdin.readline().split()))
def sorted_indexes(arr):
    return sorted(list(range(len(arr))),key=arr.__getitem__)
def printr(arr):
    [stdout.write(str(x)+' ')   for x in arr]
    cout('')
def find_lt(a, x):#'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError
def find_gt(a, x):#'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
def dist(x,y):
    return math.sqrt(x*x + y*y)
def binary_search(arr, x):
    i = bisect_left(arr, x)
    if i == len(arr) or arr[i] != x:
        return -1
    return i

# ---------------------Template ends-------------sdpt,sdpt131[Sudipta Banik]---------------------

# mp = [0]*201
# ops = [0]*201
# def go(arr,i,j ,dp):
#     if i==j and ops[i] is None:
#         return [mp[i],mp[i]]
#     if i>j:
#         return [0,0]
#     if dp[i][j]:
#         return dp[i][j]
#     mx = -1000000000
#     mn = 1000000000
#     for k in range(i+1,j,2):
#         if ops[k]:
#             left = go(arr,i,k-1,dp)
#             right = go(arr,k+1,j,dp)
#             mx = max(mx,left[0] + right[0])
#             mn = min(mn,left[1] + right[1])
#         else:
#             left = go(arr,i,k-1,dp)
#             right = go(arr,k+1,j,dp)
#             mx = max(mx,left[0] - right[1])
#             mn = min(mn,left[1] - right[0])
#     dp[i][j] = [mx,mn]
#     return [mx,mn]

    
n , a , b = readline(int)
price = [a,b]
arr = readlist(int)
half = n//2
cost = 0
flg = True
for i in range(half):
    if arr[i] == arr[n-1-i] == 2:
        cost += 2*min(a,b)
    elif arr[i] ==2 and arr[n-1-i] <= 1:
        cost += price[arr[n-1-i]]
    elif arr[i] <= 1 and arr[n-1-i] == 2:
        cost += price[arr[i]]
    elif arr[i] != arr[n-1-i]:
        flg = False
        break
if n%2 == 1:
    if arr[half] == 2:
        cost += min(a,b)
if not flg:
    print(-1)
else:
    print(cost)



    









# # def tobit(s):
# #     x = []
# #     for _ in range(3):
# #         x.append(s%2)
# #         s//=2
# #     return x

# def power(x, y, p) :
#     res = 1
#     x = x % p 
#     while (y > 0) :
#         if ((y & 1) == 1) :
#             res = (res * x) % p
#         y = y >> 1
#         x = (x * x) % p
#     return res




# def setCount(x):
#     return bin(x).count('1')

# for _ in range(var()):
    
#     a,b,n = readline()
#     p = 1000000007  
#     diff = abs(a-b)
#     mod  = power(a,n,p)
#     mod += power(b,n,p)
#     print(math.gcd(mod,diff)%p)
    
    
#     # n = var()
#     # # print(bin(n))
#     # if setCount(n)==2:
#     #     print(0)
#     # elif setCount(n)==1:
#     #     if n == 1:
#     #         print(2)
#     #     else:
#     #         print(1)
#     # elif setCount(n)==0:
#     #     print(3)
#     # else:
#     #     lo = n-1
#     #     hi = n+1
#     #     while(lo >= 3):
#     #         if(setCount(lo)==2):
#     #             break
#     #         lo -=1
#     #     while(hi <= 1000):
#     #         if(setCount(hi)==2):
#     #             break
#     #         hi +=1
        
#     #     if (hi - n) < (n - lo):
#     #         print(hi-n)
#     #     else:
#     #         print(n-lo)
        
    





# #     s = cin()
# #     t = cin()
# #     flg = False
# #     for el in range(8):
# #         bits = tobit(el)
# #         ch = []
# #         # printr(bits)
# #         for i in range(3):
# #             if bits[i]==0:
# #                 ch.append(s[i])
# #             else:
# #                 ch.append(t[i])
# #         ch.sort()
# #         if (''.join(ch) == 'bbo'):
# #             flg = True
# #             break
# #     if flg:
# #         print("yes")
# #     else:
# #         print("no")

