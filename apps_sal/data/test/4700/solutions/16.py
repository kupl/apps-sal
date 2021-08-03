n, m = map(int, input().split())
h = list(map(int, input().split()))
near = [[0] for i in h]
for i in range(m):
    a, b = map(int, input().split())
    near[a - 1].append(h[b - 1])
    near[b - 1].append(h[a - 1])
cnt = 0
for i in range(n):
    if max(near[i]) < h[i]:
        cnt += 1
print(cnt)
