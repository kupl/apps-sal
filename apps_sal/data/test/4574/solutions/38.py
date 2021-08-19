input()
a = list(map(int, input().split()))
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
d = {i: j for (i, j) in d.items() if j > 1}
if len(d) < 2:
    print(0)
else:
    d = sorted(d.items(), key=lambda x: (-x[0], -x[1]))
    print(d[0][0] * d[1][0] if d[0][1] < 4 else d[0][0] * d[0][0])
