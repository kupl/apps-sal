(n, m) = list(map(int, input().split()))
ab = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[1])
removed = -1
ans = 0
for (a, b) in ab:
    if a > removed:
        removed = b - 1
        ans += 1
print(ans)
