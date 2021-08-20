from bisect import bisect_left
(n, x) = map(int, input().split())
(s, a, b) = (0, [[], []], [[], []])
for i in range(n):
    (t, h, m) = map(int, input().split())
    a[t].append((h, m))
for t in [0, 1]:
    a[t].sort(key=lambda x: x[0])
    for (h, m) in a[t]:
        if h > x:
            break
        b[t].append(m)
    b[t].sort()
for t in [0, 1]:
    (y, i, c) = (x, [len(b[0]), len(b[1])], [b[0][:], b[1][:]])
    while c[t]:
        y += c[t].pop()
        t = 1 - t
        while i[t] < len(a[t]):
            (h, m) = a[t][i[t]]
            if h > y:
                break
            c[t].insert(bisect_left(c[t], m), m)
            i[t] += 1
    s = max(s, i[0] + i[1] - len(c[0]) - len(c[1]))
print(s)
