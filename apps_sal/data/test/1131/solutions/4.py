def f(t, c, b, w):
    a = b
    s = l = 0
    while True:
        b += w
        dt = b // x
        b -= dt * x
        s += dt
        l += 1
        if a == b:
            break
    k = c // s
    if c == k * s:
        k -= 1
    c -= k * s
    t += k * (s + l)
    while True:
        b += w
        dt = b // x
        b -= dt * x
        if c <= dt:
            return t + c
        c -= dt
        t += dt + 1


(a, b, w, x, c) = map(int, input().split())
t = b // x
if a >= c - t:
    print(c - min(c, a))
else:
    print(f(t + 1, c - t - a, b - t * x, w - x))
