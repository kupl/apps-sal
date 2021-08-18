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
print(ans)
