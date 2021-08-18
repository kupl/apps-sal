import copy
import heapq
N = int(input())
A = list(map(int, input().split()))

h1 = copy.deepcopy(A[:N])
x = sorted(A[N:])
h2 = x[N:]
x = x[:N]

now_w = sum(h1) - sum(x)
ans = now_w
used = []
heapq.heapify(h1)
heapq.heapify(h2)
heapq.heapify(used)

for i in range(N):
    now = A[N + i]
    heapq.heappush(h1, now)
    left = heapq.heappop(h1)
    while True:
        right_cand = heapq.heappop(h2)
        if len(used) > 0:
            x = heapq.heappop(used)
            if x == right_cand:
                continue
            else:
                heapq.heappush(used, x)
        break

    if right_cand >= now:
        right = right_cand
    else:
        right = now
        heapq.heappush(h2, right_cand)
        heapq.heappush(used, now)
    now_w = now_w - left + 2 * now - right
    ans = max(ans, now_w)

print(ans)
