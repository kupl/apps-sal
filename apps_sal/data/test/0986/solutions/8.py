(n, k) = (int(i) for i in input().split())
zapross = [int(i) for i in input().split()]
lave = 0
curh = set()
for i in range(n):
    if zapross[i] in curh:
        continue
    if len(curh) != k:
        lave += 1
        curh.add(zapross[i])
    else:
        lpos = -1
        cc = -1
        for j in curh:
            try:
                pos = zapross[i + 1:].index(j)
            except ValueError:
                cc = j
                break
            if pos > lpos:
                lpos = pos
                cc = j
        curh.remove(cc)
        curh.add(zapross[i])
        lave += 1
print(lave)
