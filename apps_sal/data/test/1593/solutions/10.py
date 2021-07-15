n, s = map(int, input().split())
vals = [tuple(map(int, input().split())) for i in range(n)]
vals.sort(key = lambda e: e[0]*e[0] + e[1]*e[1])
b = True
for v in vals:
    s += v[2]
    if s >= 1000000:
        print((v[0]*v[0] + v[1]*v[1])**0.5)
        b = False
        break
if b:
    print(-1)
