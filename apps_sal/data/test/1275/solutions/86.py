n, k = map(int, input().split())
k = abs(k)

ans = 0
for x in range(k + 2, 2*n + 1):
    b = min(n, x - 1)
    a = x - b
    res1 = b - a + 1

    c = min(n, x - k - 1)
    d = x - k - c
    res2 = c - d + 1
    ans += res1 * res2

print(ans)
