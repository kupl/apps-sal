import heapq
N = int(input())
A = list(map(int, input().split()))
(l, r) = ([], [])
ll = 0
for i in range(3 * N):
    if i < N:
        heapq.heappush(l, (A[i], i))
        ll += A[i]
    else:
        heapq.heappush(r, (A[i], i))
used = set()
rr = 0
for i in range(N):
    (a, idx) = heapq.heappop(r)
    used.add(idx)
    rr += a
ans = ll - rr
done = set()
for i in range(N, 2 * N):
    done.add(i)
    if A[i] > l[0][0]:
        ll -= l[0][0]
        heapq.heappop(l)
        heapq.heappush(l, (A[i], i))
        ll += A[i]
    if i in used:
        rr -= A[i]
        (a, idx) = heapq.heappop(r)
        while idx in done:
            (a, idx) = heapq.heappop(r)
        used.add(idx)
        rr += a
    ans = max(ans, ll - rr)
print(ans)
