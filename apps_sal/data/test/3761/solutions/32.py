s = input().strip()
Xs = list(map(int, input().split()))
bs = [[], []]
bb = t = 0
for c in s:
    if c == 'T':
        bs[bb].append(t)
        bb = 1 - bb
        t = 0
    else:
        t += 1
bs[bb].append(t)
rr, bs[0] = bs[0][0], bs[0][1:]
for i in range(2):
    t = 1 << 8000
    if i == 0:
        t = t << rr
    for x in bs[i]:
        t = (t << x) | (t >> x)
    if not (t >> (Xs[i] + 8000)) % 2:
        print("No")
        break
else:
    print("Yes")
