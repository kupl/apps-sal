import heapq
n = int(input())
a = list(map(int, input().split()))
score = [[0, 0] for _ in range(n + 1)]
h1 = a[0:n]
h2 = [-a[2 * n + i] for i in range(n)]
maxscore = sum(h1)
minscore = -sum(h2)
heapq.heapify(h1)
heapq.heapify(h2)
score[0][0] = maxscore
score[n][1] = minscore
for i in range(n):
    heapq.heappush(h1, a[n + i])
    heapq.heappush(h2, -a[2 * n - 1 - i])
    maxscore = maxscore + a[n + i] - heapq.heappop(h1)
    minscore = minscore + a[2 * n - 1 - i] + heapq.heappop(h2)
    score[i + 1][0] = maxscore
    score[n - 1 - i][1] = minscore
ans = -pow(10, 15)
for i in range(n + 1):
    ans = max(ans, score[i][0] - score[i][1])
print(ans)
