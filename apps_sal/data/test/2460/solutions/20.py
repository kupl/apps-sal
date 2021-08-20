(n, m) = map(int, input().split())
dist = list(map(int, input().split()))
taxists = list(map(int, input().split()))
left = [0] * (n + m)
right = [0] * (n + m)
MAX = 10000000000000000000
value = -MAX
cnt = 0
for i in range(n + m):
    if taxists[i] == 1:
        cnt += 1
        value = i
    left[i] = value
value = MAX
for i in range(n + m - 1, -1, -1):
    if taxists[i] == 1:
        value = i
    right[i] = value
answer = [0] * (n + m)
for i in range(n + m):
    if left[i] == -MAX:
        answer[right[i]] += 1
        continue
    if right[i] == MAX:
        answer[left[i]] += 1
        continue
    if abs(dist[left[i]] - dist[i]) <= abs(dist[i] - dist[right[i]]):
        answer[left[i]] += 1
    else:
        answer[right[i]] += 1
for i in answer:
    if i:
        print(i - 1, end=' ')
