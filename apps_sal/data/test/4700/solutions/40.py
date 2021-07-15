n, m = map(int, input().split())

h = list(map(int, input().split()))

ans = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    ans[a - 1] = max(ans[a - 1], h[b - 1])
    ans[b - 1] = max(ans[b - 1], h[a - 1])

anser = 0

for i in range(n):
    if ans[i] < h[i]:
        anser += 1

print(anser)
