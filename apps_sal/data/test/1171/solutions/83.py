(n, k) = list(map(int, input().split()))
v = list(map(int, input().split()))
ans = 0
for a in range(min(n, k) + 1):
    for b in range(min(n, k) - a + 1):
        c = v[:a] + v[n - b:]
        c = sorted(c)
        for i in range(k - a - b):
            if len(c) == 0:
                break
            if c[0] < 0:
                c = c[1:]
            else:
                break
        ans = max(ans, sum(c))
print(ans)
