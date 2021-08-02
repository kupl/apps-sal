n, m = list(map(int, input().split()))
bad = False
d = set()
for i in range(n):
    inp = list(input())
    s = inp.index("S")
    g = inp.index("G")
    if s < g:
        bad = True
    else:
        d.add(s - g)

if bad:
    print(-1)
else:
    print(len(d))
