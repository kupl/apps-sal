n, k, *a = map(int, open(0).read().split())
s = r = 0
for x in sorted(a)[::-1]:
    if s + x < k:
        s += x
        r += 1
    else:
        r = 0
print(r)
