n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
ans = 0
for a, b in ab:
    ans += a * min(b, m)
    m -= b
    if m <= 0:
        break
print(ans)
