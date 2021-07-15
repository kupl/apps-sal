n, h, k = map(int, input().split())
a, ai, c, t = list(map(int, input().split())), 0, 0, 0
while c > 0 or ai < n:
    while ai < n and c + a[ai] <= h:
        c += a[ai]
        ai += 1
    if c < k:
        t += 1
        c = 0
    else:
        t += c // k
        c %= k
print(t)
