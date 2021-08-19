import heapq
N, M = list(map(int, input().split()))

AB = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    AB.append((A, B))
AB = sorted(AB, key=lambda x: x[0])

hq = []
heapq.heapify(hq)  # リストhqのheap化

ans = 0
i = 0
for d in range(1, M + 1):
    while i <= N - 1 and AB[i][0] <= d:
        heapq.heappush(hq, -AB[i][1])  # heap化されたリストhqに要素xを追加
        i += 1
    if hq:
        ans -= heapq.heappop(hq)  # heap化されたリストhqから最小値を削除＆その最小値を出力
print(ans)
