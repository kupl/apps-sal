from heapq import heapify, heappop, heappush
(x, y, z, k) = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)
c = sorted(list(map(int, input().split())), reverse=True)
ans = []
for ai in a:
    for bi in b:
        ans.append(-ai - bi)
ans.sort()
ans = ans[:k] if len(ans) >= k else ans + [0] * (k - len(ans))
ans1 = []
for ci in c:
    for ansi in ans:
        heappush(ans1, ansi - ci)
for i in range(k):
    print(-heappop(ans1))
