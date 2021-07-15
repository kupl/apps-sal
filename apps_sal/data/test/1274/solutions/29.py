import heapq

N, M = list(map(int, input().split()))

AB = []
can = [[] for i in range(M+1)]
for i in range(N):
    a, b = list(map(int, input().split()))
    AB.append([a, b])
    if M - a >= 0:
        can[M-a].append(-b)

que = []
ans = 0
for i in range(M, -1, -1):
    now_list = can[i]
    for j in range(len(now_list)):
        heapq.heappush(que, now_list[j])
    if que:
        ans += heapq.heappop(que)

print((-ans))

