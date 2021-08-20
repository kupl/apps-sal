(H, W, M) = list(map(int, input().split()))
sumh = [0] * W
sumw = [0] * H
checkset = set()
for i in range(M):
    (h, w) = list(map(int, input().split()))
    checkset.add((h - 1, w - 1))
    sumh[w - 1] += 1
    sumw[h - 1] += 1
shmax = max(sumh)
swmax = max(sumw)
sh = []
sw = []
for (i, s) in enumerate(sumh):
    if s == shmax:
        sh.append(i)
for (i, s) in enumerate(sumw):
    if s == swmax:
        sw.append(i)
ans = shmax + swmax - 1
jdg = False
for i in sh:
    for j in sw:
        if (j, i) not in checkset:
            ans += 1
            jdg = True
            break
    if jdg:
        break
print(ans)
