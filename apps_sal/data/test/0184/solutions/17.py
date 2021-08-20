(l, r, a) = list(map(int, input().split(' ')))
q = min(l, r) + a
if q < max(l, r):
    print(2 * q)
else:
    print(2 * (max(l, r) + (q - max(l, r)) // 2))
