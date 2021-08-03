n, m = list(map(int, input().split()))
a, c = 0, 0

for a in range(0, min(n, int(m / 2)) + 1):
    c = max(c, a + max(0, min(int((n - a) / 2), m - 2 * a)))

print(c)
