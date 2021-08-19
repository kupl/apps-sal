import heapq
(N, K) = list(map(int, input().split()))
l = []
for i in range(N):
    l.append(list(map(int, input().split())))
l.sort()
X = []
S = 0
ans = 0
heapq.heapify(X)
for i in range(1, K + 1):
    for j in range(S, N):
        if l[j][0] <= i:
            S += 1
            heapq.heappush(X, l[j][1] * -1)
        else:
            break
    try:
        tmp = heapq.heappop(X)
        ans += tmp * -1
    except IndexError:
        continue
print(ans)
