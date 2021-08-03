import heapq

N = int(input())
a = list(map(int, input().split()))
c_que = list(map(lambda x: x * (-1), a[2 * N:]))
a_que = a[:N]

a_sum = sum(a_que)
c_sum = -sum(c_que)

heapq.heapify(a_que)
heapq.heapify(c_que)

ans = -(10**15)

score = [[0, 0] for _ in range(N + 1)]
score[0][0] = a_sum
score[N][1] = c_sum

for i in range(N):
    heapq.heappush(a_que, a[N + i])
    heapq.heappush(c_que, -a[2 * N - 1 - i])

    a_sum = a_sum + a[N + i] - heapq.heappop(a_que)
    c_sum = c_sum + a[2 * N - 1 - i] + heapq.heappop(c_que)

    score[i + 1][0] = a_sum
    score[N - 1 - i][1] = c_sum

for i in range(N + 1):
    ans = max(ans, score[i][0] - score[i][1])
print(ans)
