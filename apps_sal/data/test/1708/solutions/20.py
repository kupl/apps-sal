import sys
n, m = [int(tmp) for tmp in sys.stdin.readline().split()]
a = [0] + [int(tmp) for tmp in sys.stdin.readline().split()]
c = [0] + [int(tmp) for tmp in sys.stdin.readline().split()]

co = [tmp for tmp in range(n+1)]
co.sort(key=lambda z: c[z])
cop = 1
nb = False
for i in range(m):
    t, d = [int(tmp) for tmp in sys.stdin.readline().split()]
    if nb:
        print(0)
        continue
    s = 0
    botf = min([d, a[t]])
    a[t] -= botf
    s = botf * c[t]
    brts = d - botf
    while brts != 0:
        botf = min([brts, a[co[cop]]])
        if botf == 0:
            cop += 1
            if cop == n + 1:
                nb = True
                s = 0
                break
        a[co[cop]] -= botf
        brts -= botf
        s += botf * c[co[cop]]
    print(s)

