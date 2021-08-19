(l, p, a) = map(int, input().split())
x = min(l, p)
y = max(l, p)
if x + a > y:
    print((l + p + a) // 2 * 2)
else:
    print(2 * (x + a))
