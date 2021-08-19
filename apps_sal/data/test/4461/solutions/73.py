def f(x, y, z):
    return max(x, y, z) - min(x, y, z)


(h, w) = list(map(int, input().split()))
l = []
(ans1, ans2) = (h * w, h * w)
for i in range(1, h // 2 + 1):
    s1 = i * w
    s2 = w * ((h - i) // 2)
    s3 = h * w - s1 - s2
    s4 = (h - i) * (w // 2)
    s5 = h * w - s1 - s4
    ans1 = min(ans1, f(s1, s2, s3), f(s1, s4, s5))
for i in range(1, w // 2 + 1):
    s1 = i * h
    s2 = h * ((w - i) // 2)
    s3 = h * w - s1 - s2
    s4 = (w - i) * (h // 2)
    s5 = h * w - s1 - s4
    ans2 = min(ans2, f(s1, s2, s3), f(s1, s4, s5))
print(min(ans1, ans2))
