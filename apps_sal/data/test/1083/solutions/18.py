n = int(input())
l = range(1, n + 1)
s = (n + 1) * n // 2
print(s % 2)
t = 0
tp = []
pt = -1
while not (s // 2 - t in l and s // 2 - t not in tp):
    t += l[pt]
    tp.append(l[pt])
    pt -= 1
tp.append(s // 2 - t)
print(len(tp), ' '.join((str(i) for i in tp)))
