n, m, s, d = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
points = [0, a[0] - 1]
if d == 1 or a[0] - 1 < s:
    print("IMPOSSIBLE")
    return
for i in range(0, n):
    if a[i] - a[i - 1] - 2 < s:
        if a[i] + 1 - points[-1] > d:
            print("IMPOSSIBLE")
            return
    else:
        points.append(a[i - 1] + 1)
        points.append(a[i] - 1)

points.append(a[-1] + 1)
for i in range(1, len(points)):
    if i % 2 == 1:
        print("RUN", points[i] - points[i - 1])
    else:
        print("JUMP", points[i] - points[i - 1])
if a[-1] + 1 != m:
    print("RUN", m - 1 - a[-1])
