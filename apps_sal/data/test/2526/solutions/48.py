import heapq
(X, Y, A, B, C) = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P.sort(reverse=True)
P = P[:X]
Q.sort(reverse=True)
Q = Q[:Y]
sp = sum(P)
sq = sum(Q)
ans = sp + sq
R.sort(reverse=True)
heapq.heapify(P)
heapq.heapify(Q)
p = heapq.heappop(P)
q = heapq.heappop(Q)
r = R.pop(0)
while p < r or q < r:
    if r - p > r - q:
        heapq.heappush(P, r)
        ans += r - p
        p = heapq.heappop(P)
    else:
        heapq.heappush(Q, r)
        ans += r - q
        q = heapq.heappop(Q)
    if len(R) == 0:
        break
    r = R.pop(0)
print(ans)
