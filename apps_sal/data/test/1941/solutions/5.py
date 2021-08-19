import math
s = input()
(a, b, n) = s.split()
(a, b, n) = (int(a), int(b), int(n))
for cas in range(0, n):
    s = input()
    (l, t, m) = s.split()
    (l, t, m) = (int(l), int(t), int(m))
    (L, R) = (l, (t - a) // b + 1)
    if R < L:
        print(-1)
        continue
    else:
        A = b
        B = 2 * a - b
        C = (2 * a + b * l - 2 * b) * (1 - l) - 2 * t * m
        ans = (-B + math.sqrt(B * B - 4 * A * C)) / 2 / A
        if ans > R:
            ans = R
        print(int(ans))
