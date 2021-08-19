(n, m) = map(int, input().split())
d = [0] * (n + 1)
ac = 0
wa = 0
for i in range(m):
    (p, s) = input().split()
    p = int(p)
    if d[p] == -1:
        continue
    elif s == 'AC':
        ac += 1
        wa += d[p]
        d[p] = -1
    else:
        d[p] += 1
print(ac, wa)
