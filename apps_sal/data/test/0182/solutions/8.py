a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
a -= x
b -= y
c -= z
a, b, c = sorted([a, b, c])
k = max(0, c // 2)
c -= min(2 * k, -2 * a)
a += min(k, -a)
if a < 0:
    k = max(0, b // 2)
    b -= min(2 * k, -2 * a)
    a += min(k, -a)
elif b < 0:
    k = max(0, c // 2)
    c -= min(2 * k, -2 * b)
    b += min(k, -b)
if a >= 0 and b >= 0 and c >= 0:
    print("Yes")
else:
    print("No")
