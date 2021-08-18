x, y, l, r = list(map(int, input().split()))
bad = []
for i in range(61):
    for j in range(61):
        cr = x ** i + y ** j
        if l <= cr <= r:
            bad.append(x ** i + y ** j)
bad = [l] + bad + [r]
bad.sort()
mx = 0
if len(bad) == 2:
    print(max(mx, bad[1] - bad[0] + 1))
    return
for i in range(len(bad) - 1):
    cr = bad[i + 1] - bad[i] - 1
    if i == 0 or i == len(bad) - 2:
        cr += 1
    mx = max(mx, cr)
print(mx)
