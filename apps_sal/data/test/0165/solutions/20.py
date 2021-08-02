b, d, s = list(map(int, input().split()))
a1, a2, a3, a4 = 0, 0, 0, 0


if max(b, s, d) == b:
    if d < b - 1 and s != max(b, s, d):
        a1 += b - 1 - d
    if d < b - 1 and s == max(b, s, d):
        a1 += b - d
    if s < b - 1:
        a1 += b - 1 - s
elif max(b, s, d) == d:
    a1 += d - b
    if s < d - 1:
        a1 += d - 1 - s
elif max(b, s, d) == s:
    a1 += s - d
    a1 += s - b

b1, d1, s1 = d, s, b
if max(b1, s1, d1) == b1:
    if d1 < b1 - 1 and s1 != max(b1, s1, d1):
        a2 += b1 - 1 - d1
    if d1 < b1 - 1 and s1 == max(b1, s1, d1):
        a2 += b1 - d1
    if s1 < b1 - 1:
        a2 += b1 - 1 - s1
elif max(b1, s1, d1) == d1:
    a2 += d1 - b1
    if s1 < d1 - 1:
        a2 += d1 - 1 - s1
elif max(b1, s1, d1) == s1:
    a2 += s1 - d1
    a2 += s1 - b1

b, d, s = s, b, d
if max(b, s, d) == b:
    if d < b - 1 and s != max(b, s, d):
        a3 += b - 1 - d
    if d < b - 1 and s == max(b, s, d):
        a3 += b - d
    if s < b - 1:
        a3 += b - 1 - s
elif max(b, s, d) == d:
    a3 += d - b
    if s < d - 1:
        a3 += d - 1 - s
elif max(b, s, d) == s:
    a3 += s - d
    a3 += s - b
print(min(a1, a2, a3))
