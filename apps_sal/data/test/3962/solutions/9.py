import heapq
n = int(input())
fa = [i for i in range(n)]
ls = []
rs = []
for i in range(n):
    l, r = [int(x) for x in input().split()]
    ls.append((l, i))
    rs.append((r, i))
ls.sort()
rs.sort()
ans = n
for i in range(n):
    ans += max(ls[i][0], rs[i][0])
# heapq.heapify(ls)
# heapq.heapify(rs)
#
# ans=n
# if n==1:
#     print(max(ls[0][0],rs[0][0])+1)
#     quit()
# for i in range(n):
#     ll=heapq.heappop(ls)
#     if fa[rs[0][1]]!=fa[ll[1]]:
#         rr=heapq.heappop(rs)
#         fa[ll[1]]=rr[1]
#     else:
#         tem=heapq.heappop(rs)
#         rr=heapq.heappop(rs)
#         fa[ll[1]]=rr[1]
#         heapq.heappush(rs,tem)
#     ans+=max(ll[0],rr[0])
print(ans)
