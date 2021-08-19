(x, y, l, r) = map(int, input().split())
v = [l - 1, r + 1]
for a in range(0, 60):
    if x ** a > r:
        break
    for b in range(0, 60):
        if y ** b > r:
            break
        if l <= x ** a + y ** b <= r:
            v += [x ** a + y ** b]
v.sort()
ans = 0
for i in range(len(v) - 1):
    ans = max(ans, v[i + 1] - v[i] - 1)
print(ans)
