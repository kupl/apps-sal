l, r, a = map(int, input().split())
if l > r: l, r = r, l
if l + a <= r:
    print(2 * (l + a))
else:
    k = r - l
    a -= k
    l += k
    print(2 * l + a - a % 2)
