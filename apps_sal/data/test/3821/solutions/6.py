import sys

input()
ps = sorted((float(p) for p in input().split()), reverse=True)
if 1.0 in ps:
    print(1)
    return
a, b = 0, 1
for p in ps:
    c, d = a + p / (1 - p), b * (1 - p)
    if c * d > a * b:
        a, b = c, d
    else:
        break
print('{:.9}'.format(a * b))

