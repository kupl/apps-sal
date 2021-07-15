x, y, l, r = map(int, input().split(' '))
a = []
for i in range(65):
    for j in range(65):
        t = x**i + y**j
        if t <= r and t >= l:
            a.append(t)
a.sort()
if len(a) == 0:
    print(r - l + 1)
    return
ans = max(a[0] - l, r - a[-1])
for i in range(1, len(a)):
    ans = max(ans, a[i]-a[i-1]-1)

print(ans)
