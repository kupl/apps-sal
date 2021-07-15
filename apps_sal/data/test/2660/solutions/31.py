import heapq
Q = int(input())
ans = 0
L = []
R = []
for _ in range(Q):
    q = input()
    if q[0] == '1':
        _, a, b = map(int, q.split())
        ans += b
        if len(L) > 0 and not -L[0] <= a <= R[0]:
            ans += min(abs(a + L[0]), abs(a - R[0]))
        l = heapq.heappushpop(L, -a)
        r = heapq.heappushpop(R, a)
        heapq.heappush(L, -r)
        heapq.heappush(R, -l)
    else:
        print(-L[0], ans)
