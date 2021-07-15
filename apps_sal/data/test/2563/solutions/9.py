t = int(input())
for _ in range(t):
    ev = []
    od = []
    s = map(int,list(input()))
    for v in s:
        if v % 2:
            od.append(v)
        else:
            ev.append(v)
    ev.append(1000)
    od.append(1000)
    ep = 0
    op = 0
    while ep < len(ev)-1 or op < len(od)-1:
        if ev[ep] < od[op]:
            print(ev[ep],end='')
            ep += 1
        else:
            print(od[op],end='')
            op += 1
    print("")

