p, q, l, r = list(map(int, input().split()))
a = [0] * p
b = [0] * p
c = [0] * q
d = [0] * q
for i in range(p):
    a[i], b[i] = list(map(int, input().split()))
for i in range(q):
    c[i], d[i] = list(map(int, input().split()))
cnt = 0
for t in range(l, r + 1):
    events = \
        list([(x + 0, +1) for x in a]) + \
        list([(x + 0, -1) for x in b]) + \
        list([(x + t, +1) for x in c]) + \
        list([(x + t, -1) for x in d])
    events.sort(key=lambda x: (x[0], -x[1]))
    online = 0
    for _, i in events:
        online += i
        if online > 1:
            cnt += 1
            break
print(cnt)

