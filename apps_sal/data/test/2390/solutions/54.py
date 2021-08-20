import heapq
(N, C) = map(int, input().split())
sushi = []
for i in range(N):
    cur_sushi = list(map(int, input().split()))
    sushi.append(cur_sushi)
(sum_V, sum_right) = ([0], [0])
for i in range(N):
    sum_V.append(sum_V[i] + sushi[i][1])
    sum_right.append(sum_V[i + 1] - sushi[i][0])
(sum_V, sum_left) = ([0], [0])
for i in range(N):
    sum_V.append(sum_V[i] + sushi[N - 1 - i][1])
    sum_left.append(sum_V[i + 1] - (C - sushi[N - 1 - i][0]))
ans = max(max(sum_left), max(sum_right))
left = [0]
heapq.heapify(left)
for l in range(N):
    now = sum_right[N - l] - sushi[N - 1 - l][0]
    heapq.heappush(left, -sum_left[l])
    now -= left[0]
    ans = max(ans, now)
right = [0]
heapq.heapify(right)
for r in range(N):
    now = sum_left[N - r] - (C - sushi[r][0])
    heapq.heappush(right, -sum_right[r])
    now -= right[0]
    ans = max(ans, now)
print(ans)
