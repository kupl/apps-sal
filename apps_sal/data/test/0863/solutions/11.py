from math import ceil, floor

a, ta = map(int, input().split())
b, tb = map(int, input().split())
h, m = map(int, input().split(":"))

mi = 0
ma = 23 * 60 + 59 - 5 * 60
cur = (h - 5) * 60 + m

start = min(ma, max(cur - tb, 0))
end = max(mi, min(ma, cur + ta))

start = ceil(start / b) * b
end = floor(end / b) * b

r = int((end - start) / b) + 1

if start == cur - tb:
    r -= 1

if end == cur + ta:
    r -= 1

print(r)
