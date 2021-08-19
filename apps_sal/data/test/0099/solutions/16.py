def miis():
    return list(map(int, input().split()))


(b, q, l, m) = miis()
(*a,) = miis()
c = 0
for _ in ' ' * 100:
    if abs(b) > l:
        break
    if b not in a:
        c += 1
    b *= q
if c < 35:
    print(c)
else:
    print('inf')
