from heapq import heappop, heappush
inf = float('inf')

N = int(input())
A = list(map(int, input().split()))

l = []
res = 0
for i in range(N):
    heappush(l, A[i])
    res += A[i]
ls = []
ls.append(res)

for i in range(N, 2 * N):
    heappush(l, A[i])
    res += A[i]
    res -= heappop(l)
    ls.append(res)

A.reverse()

s = []
res = 0
for i in range(N):
    heappush(s, -A[i])
    res += A[i]
ss = []
ss.append(res)

for i in range(N, 2 * N):
    heappush(s, -A[i])
    res += A[i]
    res -= -heappop(s)
    ss.append(res)

ss.reverse()

ans = -inf

for i in range(N + 1):
    score = ls[i] - ss[i]
    ans = max(ans, score)

print(ans)
