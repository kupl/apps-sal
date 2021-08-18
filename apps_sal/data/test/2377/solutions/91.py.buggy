from heapq import heappop, heappush

N, H = map(int, input().split())
a = [None] * N
b = [None] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())

a.sort()
b.sort()
q = []
for i in range(N):
    if b[i] > a[-1]:
        heappush(q, -b[i])

ans = 0
while q:
    H += heappop(q)
    ans += 1
    if H <= 0:
        print(ans)
        return

print(ans + (H + a[-1] - 1) // a[-1])
