n, k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])

ans = float("inf")
for i in range(n - k + 1):
    sa = h[i + k - 1] - h[i]
    if ans > sa:
        ans = sa

print(ans)
