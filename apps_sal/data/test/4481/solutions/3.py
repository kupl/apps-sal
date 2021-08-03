N = int(input())
d = {}
for _ in range(N):
    p = input()
    if p in d:
        d[p] += 1
    else:
        d[p] = 1
ma = max(d.values())
d2 = sorted(d.items())
d.clear()
d.update(d2)
for k, v in list(d.items()):
    if v == ma:
        print(k)
