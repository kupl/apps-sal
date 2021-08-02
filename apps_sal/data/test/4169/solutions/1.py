n, m = list(map(int, input().split()))

s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort()

ans = 0
for a, b in s:
    ans += min(a * b, a * m)
    m -= b
    if m <= 0:
        break

print(ans)
