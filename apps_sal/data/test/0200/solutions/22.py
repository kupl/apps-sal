(h, g) = [int(x) for x in input().split(' ')]
(a, b) = [int(x) for x in input().split(' ')]
ans = 0
h += 8 * a
uph = h
while g > h:
    ans += 1
    h += 12 * (a - b)
    if h <= uph:
        ans = -1
        break
    uph = h
print(ans)
