import heapq
n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))
q = []
melted = 0
for (snow, temp) in zip(v, t):
    heapq.heappush(q, snow + melted)
    answer = 0
    while q and q[0] <= melted + temp:
        answer += q[0] - melted
        heapq.heappop(q)
    answer += temp * len(q)
    print(answer, end=' ')
    melted += temp
