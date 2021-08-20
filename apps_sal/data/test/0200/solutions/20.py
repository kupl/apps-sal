(h1, h2) = map(int, input().split())
(a, b) = map(int, input().split())
(d, v) = (h2 - h1 - 8 * a, 12 * (a - b))
if d <= 0:
    print(0)
elif b >= a:
    print(-1)
else:
    print((d + v - 1) // v)
