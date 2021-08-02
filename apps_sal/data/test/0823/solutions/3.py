x, y = map(int, input().split())
u, v = abs(x), abs(y)
a = max(u, v)
s = 4 * (a - 1)

if u >= v and x > 0 and y > 1 - a:
    s += 1
elif v >= u and y > 0:
    s += 2
elif u >= v and x < 0:
    s += 3
elif v >= u and y < 0:
    s += 4

print(s if a > 0 else 0)
