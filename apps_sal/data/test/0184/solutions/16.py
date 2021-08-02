l, r, a = [int(x) for x in input().split()]
if l > r:
    r, l = l, r

print(2 * (l + a if l + a < r else (l + r + a) // 2))
