b, l, d = map(int, input().split())

m = max(b, l, d)
x = m - 1
missing = 0
if x - b > 0:
    missing += x - b
if x - l > 0:
    missing += x - l
if x - d > 0:
    missing += x - d

print(missing)
