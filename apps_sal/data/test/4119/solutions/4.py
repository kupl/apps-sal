import heapq
(N, M) = list(map(int, input().split()))
X = list(map(int, input().split()))
if N >= M:
    ans = 0
else:
    X.sort()
    distance = [0] * (M - 1)
    for i in range(M - 1):
        distance[i] = -abs(X[i + 1] - X[i])
    sum_distance = sum(distance)
    heapq.heapify(distance)
    count = 0
    for _ in range(N - 1):
        max_num = heapq.heappop(distance)
        count += max_num
    ans = abs(sum_distance - count)
print(ans)
