(n, m) = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)])
(ans, l) = (0, m)
for (a, b) in ab:
    if b > l:
        ans += l * a
        break
    ans += b * a
    l -= b
print(ans)
