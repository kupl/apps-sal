
c, v0, v1, a, l = list(map(int, input().split()))

v = v0
t = 1
last = v0

if last >= c:
    print(1)
    return

while last < c:
    v = min(v1, v0 + t * a) - l
    last += v
    t += 1

print(t)
