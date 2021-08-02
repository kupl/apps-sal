[n, a], c = list(map(int, input().split())), [0] + list(map(int, input().split()))
ans = 0
for d in range(max(a, n - a + 1)):
    directions = found = 0
    if a - d > 0:
        directions += 1
        found += c[a - d]
    if a + d <= n and d:
        directions += 1
        found += c[a + d]
    ans += (directions == found) * found
print(ans)
