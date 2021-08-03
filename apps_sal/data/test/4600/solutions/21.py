n, m = map(int, input().split())
ps = [list(input().split()) for _ in range(m)]

c = [0] * n
for p, s in ps:
    if s == 'AC':
        c[int(p) - 1] = 1
d = [0] * n
wa = 0
ac = 0
for p, s in ps:
    if d[int(p) - 1] == 0:
        if s == 'WA':
            if c[int(p) - 1] == 1:
                wa += 1
        else:
            ac += 1
            d[int(p) - 1] = 1
print(ac, wa)
