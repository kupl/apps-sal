from collections import Counter
h, w, m = list(map(int, input().split()))
blist = [list(map(int, input().split())) for _ in range(m)]

blist_set = set(map(tuple, blist))

rowdict = Counter([blist[i][0] for i in range(m)])
coldict = Counter([blist[i][1] for i in range(m)])

maxr = rowdict.most_common()[0][1]
maxr_keys = []
for i in rowdict.most_common():
    if i[1] == maxr:
        maxr_keys.append(i[0])
    else:
        break
maxc = coldict.most_common()[0][1]
maxc_keys = []
for i in coldict.most_common():
    if i[1] == maxc:
        maxc_keys.append(i[0])
    else:
        break

for i in maxr_keys:
    for j in maxc_keys:
        if (i, j) not in blist_set:
            print((maxr + maxc))
            break
    else:
        continue
    break
else:
    print((maxr + maxc - 1))
