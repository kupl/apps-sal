from heapq import heappop, heappush
N, M = list(map(int, input().split()))
score = 0
AB = [[] for i in range(M)]
for i in range(N):
    a, b = list(map(int, input().split()))
    if M - a >= 0:
        AB[M - a].append(b)

# print(AB)
queue = []
for i in range(1, M + 1):
    for j in AB[-i]:
        heappush(queue, -j)
    if queue != []:
        score += -1 * heappop(queue)

    #print(score, queue)
print(score)
