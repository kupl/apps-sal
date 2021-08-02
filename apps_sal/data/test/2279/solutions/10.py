import heapq

n = int(input()) * 2
ans = [-1] * (n + 1)

h = []

for i in range(2, n + 1):
    j = 1
    for e in input().split():
        x = int(e)
        heapq.heappush(h, [-x, i, j])
        j += 1

i = 1
while True:
    cur = heapq.heappop(h)
    if ans[cur[1]] == -1 and ans[cur[2]] == -1:
        ans[cur[1]] = cur[2]
        ans[cur[2]] = cur[1]

    while ans[i] != -1 and i < n:
        i += 1
    if i == n:
        break

print(*ans[1:])
