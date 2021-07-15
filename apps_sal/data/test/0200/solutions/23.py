h, g = map(int, input().split())
a, b = map(int, input().split())
ans = 0
h += a << 3
uph = h
while g > h:
    ans += 1
    h += 12 * (a - b)
    if h <= uph:
        ans = -1
        break
    uph = h
print(ans)
