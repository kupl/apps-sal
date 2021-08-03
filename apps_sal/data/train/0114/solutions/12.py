import sys
sin = sys.stdin
t = int(sin.readline())
for _ in range(t):
    n = int(sin.readline())
    monpows = [int(x) for x in sin.readline().split()]
    m = int(sin.readline())
    endtopow = dict()
    maxhero = 0
    for _ in range(m):
        h = [int(x) for x in sin.readline().split()]
        maxhero = max(maxhero, h[0])
        if h[1] in endtopow:
            endtopow[h[1]] = max(h[0], endtopow[h[1]])
        else:
            endtopow[h[1]] = h[0]
    endurances = [0 for x in range(n + 2)]
    for i in range(len(endurances) - 2, -1, -1):
        if i in endtopow:
            endurances[i] = max(endurances[i + 1], endtopow[i])
        else:
            endurances[i] = endurances[i + 1]
    days = 0
    msofar = 0
    maxpow = 0
    i = 0
    cant = False
    while i < n:
        maxpow = max(maxpow, monpows[i])
        if maxpow > maxhero:
            cant = True
            break
        if maxpow <= endurances[msofar + 1]:
            i += 1
            msofar += 1
        else:
            msofar = 0
            maxpow = 0
            days += 1
    days += 1
    if not cant:
        print(days)
    else:
        print(-1)
