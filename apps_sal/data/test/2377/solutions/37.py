from math import ceil
n, h, *AB = map(int, open(0).read().split())
a = max(AB[::2])
B = sorted(b for b in AB[1::2] if a < b)[::-1]
c = 0
for b in B:
    h -= b
    c += 1
    if h <= 0:
        break
else:
    c += ceil(h / a)
print(c)
