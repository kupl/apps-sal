t = int(input())
for _ in range(t):
    (x0, y0) = input().split()
    (x0, y0) = (int(x0), int(y0))
    c = [0] + list(map(int, input().split()))
    c[0] = c[-1]
    c.append(c[1])
    for i in range(1, 7):
        c[i] = min(c[i], c[i - 1] + c[i + 1])
    c[7] = c[1]
    s = (None, [1, 1], [0, 1], [-1, 0], [-1, -1], [0, -1], [1, 0], [1, 1])
    ans = 1e+30
    for i in range(1, 7):
        (x1, y1) = s[i]
        (x2, y2) = s[i + 1]
        a = (x0 * y2 - y0 * x2) // (x1 * y2 - y1 * x2)
        b = (x0 * y1 - y0 * x1) // (x2 * y1 - y2 * x1)
        if a >= 0 and b >= 0:
            ans = min(ans, a * c[i] + b * c[i + 1])
    print(ans)
