(a, ta) = list(map(int, input().split()))
(b, tb) = list(map(int, input().split()))
(h, m) = list(map(int, input().split(':')))
time = (h - 5) * 60 + m
r = time % b
if r >= tb:
    t2 = time + b - r
else:
    t2 = time - r - b * ((time - r - max(time - tb + 1, 0)) // b)
t3 = min(time + ta, 19 * 60) - 1
if t3 < t2:
    print(0)
else:
    print((t3 - t2) // b + 1)
