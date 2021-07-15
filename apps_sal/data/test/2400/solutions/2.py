from bisect import bisect
from collections import defaultdict
# l = list(map(int,input().split()))
# map(int,input().split()))
from math import gcd,sqrt,ceil,inf
from collections import Counter
import sys
sys.setrecursionlimit(1000000)
from bisect import bisect
from collections import defaultdict
# l = list(map(int,input().split()))
# map(int,input().split()))
from math import gcd,sqrt,ceil,inf,factorial,log2
from collections import Counter
# import sys
# sys.setrecursionlimit(10**9)
#
#
# def update(i,z,bit):
#
#     # print(i)
#     while i<len(bit):
#         bit[i]+=z
#         i+=i&-i
#         # print(i)
# def query(i,bit):
#     sum = 0
#
#     while i>0:
#         sum+=bit[i]
#         i-=i&-i
#
#     return sum
#
#
# n,q = map(int,input().split())
#
# l = list(map(int,input().split()))
# bit = [0]*(n+1)
# for i in range(n):
#     update(i+1,l[i],bit)
# pref = [0]
# la = l.copy()
# la.reverse()
# for i in la:
#     pref.append(pref[-1]+i)
#
# bit2 = [0]*(n+1)
# for i in range(n):
#     update(i+1,la[i],bit2)
#
# for _ in range(q):
#     yo = list(map(int,input().split()))
#     if la[0] == 1:
#         a,b,c,d = yo
#         x,y = c,d
#         i = b
#         z1 = (query(y,bit) - query(x-1,bit))*(x-i)
#         x+=1
#         i = n-y
#         j = n-x
#         z2 = (query(j,bit2) - query(i-1,bit2))
#         print(z1-z2)
#     else:
#         a,b,c = yo
#         update(b,c,bit)
#         z1 = query(n,bit2) - query(b-1,bit2)
#         j = n-b
#         update(j,z1,bit2)



t = int(input())

for i in range(t):
    n = int(input())
    l1 = list(map(int,input().split()))
    m = int(input())
    l2 =  list(map(int,input().split()))
    count1 = 0
    for i in l2:
        if i%2 == 0:
            count1+=1
    count2 = m-count1
    ans = 0
    for i in l1:
        if i%2 == 0:
            ans+=count1
        else:
            ans+=count2
    print(ans)



