t, s, x = list(map(int, input().split()))

if x == t:
    print("YES")
    return

if x < t:
    print("NO")
    return

t += s
d = int((x - t) / s)

if d > 0:
    d -= 1

x -= d * s

while t <= x:
    if t == x or t + 1 == x:
        print("YES")
        return
    t += s

print("NO")
