(n, m) = map(int, input().split())
h = list(map(int, input().split()))
ab = [map(int, input().split()) for _ in range(m)]
(a, b) = [list(i) for i in zip(*ab)]
Max = []
for i in range(n):
    Max.append(0)
ans = 0
for i in range(m):
    Max[a[i] - 1] = max(Max[a[i] - 1], h[b[i] - 1])
    Max[b[i] - 1] = max(Max[b[i] - 1], h[a[i] - 1])
for i in range(n):
    if h[i] > Max[i]:
        ans += 1
print(ans)
