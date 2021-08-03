

from collections import defaultdict
n, k = list(map(int, input().split()))

la = list(map(int, input().split()))

# l = []
#
# for i in range(len(la)):
#        l.append([la[i],i])
# l.sort()
mini = 10**18
# i = 0
# j = len(l)-1
# # print(l)
# while i<j:
#     if l[i][0]+l[j][0]<k:
#         i+=1
#     elif l[i][0]+l[j][0]>k:
#         j-=1
#     else:
#         if l[i][0]+l[j][0]==k:
#
#             z1,z2 = max(l[i][1],l[j][1]),min(l[i][1],l[j][1])
#             ans1 = max(z1,z2)+1
#             ans2 = max(n-z1,n-z2)
#             ans3 = max(n-z1,z2+1)
#             ans4 = max(z1+1,n-z2)
#             # print(l[i][0],l[j][0])
#             if l[i][0]!=l[j][0]:
#              mini = min(mini,ans1,ans2,ans3,ans4)
#             j-=1
#             i+=1
#
# if mini == 10**18:
#     print(-1)
# else:
#     print(mini)

#
# from collections import defaultdict
# INF = float("inf")
#
# n,k = map(int,input().split())
# t = list(map(int,input().split()))
# d = defaultdict(int)
# for i in range(n):
#     x = i+1 if i<n/2 else n-i
#     if d[t[i]]:
#         d[t[i]] = min(d[t[i]],x)
#     else:
#         d[t[i]] = x
# ans = INF
# for i in range(n):
#     if d[k-t[i]] and t[i] != k-t[i]:
#         ans = min(ans,max(d[k-t[i]],d[t[i]]))
# print(-1 if ans == INF else ans)
#
#
#

hash = defaultdict(int)

for i in range(len(la)):
    z1 = i + 1
    z2 = n - i
    z = min(z1, z2)
    if la[i] in hash:
        hash[la[i]] = min(z, hash[la[i]])
    else:
        hash[la[i]] = z

for i in range(len(la)):
    z = k - la[i]
    if z in hash and z != la[i]:
        ans = max(hash[z], hash[la[i]])
        mini = min(mini, ans)


if mini == 10**18:
    print(-1)
else:
    print(mini)
