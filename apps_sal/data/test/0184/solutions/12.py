(l, r, a) = map(int, input().split())
(l, r) = (max(l, r), min(l, r))
if l - r >= a:
    print((r + a) * 2)
else:
    print(2 * l + (a - (l - r)) // 2 * 2)
