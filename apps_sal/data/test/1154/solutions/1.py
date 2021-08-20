(n, h, k) = list(map(int, input().split()))
xs = list(map(int, input().split())) + [h + 1]
t = 0
x = 0
i = 0
while i + 1 < len(xs) or x > 0:
    while x + xs[i] <= h:
        x += xs[i]
        i += 1
    d = max(1, min(x, x - h + xs[i] + k - 1) // k)
    x = max(0, x - d * k)
    t += d
print(t)
