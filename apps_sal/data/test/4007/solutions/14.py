from math import sqrt, factorial, gcd, log2, inf, ceil
import heapq
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right
import sys
from sys import stdin
from collections import deque
mod = 10**9 + 7
# def rl():
#     return [int(w) for w in stdin.readline().split()]
# map(int,input().split())
# # l = list(map(int,input().split()))
# from itertools import permutations

# n,k = map(int,input().split())
# x = int(input())
# s = str(x)
#
# ans = ['0']*n
#
# flag = 0
#
# for i in range(n):
#   if i-k>=0:
#       ans[i] = ans[i-k]
#       if ans[i]<s[i]:
#           flag = 1
#           break
#   else:
#       ans[i] = s[i]
# s1 = ''.join(ans)
# if not flag:
#     print(n)
#     print(s1)
#     return
# flag = 0
# ans = ['0']*n
#
# for i in range(k-1,-1,-1):
#     if s[i] == '9':
#         continue
#     else:
#         ans[i] = str(int(s[i]) + 1)
#         flag = 1
#
#         for j in range(i+1,k-1):
#             ans[j] = '0'
#         for j in range(i):
#             ans[j] = s[j]
#         break
# if flag:
#
#  for i in range(k,n):
#    if i-k<0:
#      continue
#
#    else:
#        ans[i] = ans[i-k]
#
#
#  print(len(ans))
#  print(''.join(ans))
#
# else:
#
#     if s[0] != '9':
#         for i in range(n):
#             if i-k<0:
#               if i == 0:
#                  ans[i] = str(int(s[i]) + 1)
#               else:
#                   ans[i] = '0'
#             else:
#                 ans[i] = ans[i-k]
#         print(len(ans))
#         print(''.join(ans))
#     else:
#         # print(ans)
#         ans+=['0']
#         for i in range(n+1):
#             if i-k<0:
#                 if i == 0:
#                     ans[i] = '1'
#                 else:
#                     ans[i] = '0'
#             else:
#                 ans[i] = ans[i-k]
#         print(len(ans))
#         print(''.join(ans))
#
#


#
# t = int(input())
#
# for _ in range(t):
#
#     n,s = map(int,input().split())
#     l = list(map(int,input().split()))
#     pa = []
#     ans = 0
#     if sum(l)<=s:
#         print(0)
#         continue
#     for i in range(n-1):
#
#         if l[i]>l[i+1]:
#             if pa == []:
#               pa.append(l[i])
#               ans = i+1
#             else:
#                if pa[0]<l[i] and s-pa[0]>=0:
#
#                    s-=pa[0]
#                    pa.pop()
#                    pa.append(l[i])
#                    ans = i+1
#                    if s == 0:
#                        break
#                else:
#                    if s>=l[i]:
#                        s-=l[i]
#                    else:
#                        break
#
#         else:
#             if s>=l[i]:
#                 s-=l[i]
#             else:
#                 break
#
#     print(ans)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# t = int(input())
#
# for _ in range(t):
#
#     n,m = map(int,input().split())
#     l1 = list(map(int,input().split()))
#     l2 = list(map(int,input().split()))
#     hash = defaultdict(int)
#
#     seti = set(l2)
#     for i in range(n):
#         if l1[i] in seti:
#             hash[l1[i]] = i
#     st = []
#     ans = 0
#     s = set(l1)
#     for i in range(m):
#           if l2[i] in s:
#              if st == []:
#                  z = hash[l2[i]]
#                  st.append(z)
#                  ans+=2*z + 1
#              else:
#                  z = hash[l2[i]]
#                  # print(i,z)
#                  if st[0]>z:
#                      ans+=1
#                  else:
#                      ans+=2*(z-1)+1
#                      st.pop()
#                      st.append(z-1)
#
#     print(ans)
#
#
#


n = int(input())
l = list(map(int, input().split()))
la = [i + 1 for i in range(n)]
s = set(la)
yo = set()
for i in l:
    if i is not 0:
        s.remove(i)
        yo.add(i)
k = list(s)
k.sort()
for i in range(n):
    if l[i] == 0:
        z = k.pop()
        l[i] = z

for i in range(n):
    if l[i] == i + 1:

        for j in range(n):
            if l[j] not in yo:
                if l[j] == j + 1 and i != j:
                    l[i], l[j] = l[j], l[i]
                    break
                else:
                    if l[j] != i + 1 and l[i] != j + 1:
                        l[i], l[j] = l[j], l[i]
                        break

        break

print(*l)
