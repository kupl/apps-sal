n, x = map(int, input().split())
l = list(map(int, input().split()))
dist = [0] * (n + 1)
for i in range(1, n + 1):
    dist[i] = dist[i - 1] + l[i - 1]

cnt = 0
for i in range(n + 1):
    if dist[i] <= x:
        cnt += 1
print(cnt)
