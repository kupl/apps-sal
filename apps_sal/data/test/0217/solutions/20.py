a, b, f, k = [int(i) for i in input().split()]

ff = [0]

for i in range(k):
    d = f
    if i % 2 == 1:
        d = a - f
    ff.append(i * a + d)

ff.append(k * a)

stops = 0

while len(ff) > 0:
    next = 0
    if ff[0] == k * a:
        break
    while ff[next + 1] - ff[0] <= b:
        next += 1
        if ff[next] == k * a:
            break
    if next == 0:
        print("-1")
        return
    if ff[next] != k * a:
        stops += 1
        while next > 0:
            ff.pop(0)
            next -= 1
    else:
        break
print(stops)
