#!/usr/bin/env python3
def ri():
    return list(map(int, input().split()))

n, k = ri()

t = list(ri())
tt = []
mc = 0
for i in range(n):
    if i == 0:
        if t[i] < 0:
            tt.append(-1)
            mc += 1
        else:
            tt.append(1)
        continue
    if t[i] < 0:
        mc += 1
        if t[i-1] >= 0:
            tt.append(-1)
        continue
    else:
        if t[i-1] >= 0:
            tt[-1] = tt[-1] + 1
        else:
            tt.append(1)
if mc > k:
    print(-1)
    return
if tt[0] != -1:
    tt = tt[1:]

if len(tt) == 0:
    print(0)
    return

ttt = []
maxs = len(tt)
k2 = k
tt2 = tt[:]

# exclude last tt
if tt[-1] != -1:
    tt = tt[:-1]

for i in tt:
    if i > 0:
        ttt.append(i)
k -= mc
ttt.sort()
for i in ttt:
    if k -i >= 0:
        k -= i
        maxs -= 2
    else:
        break

# include last tt
ttt2 = []
maxs2 = len(tt2)
for i in tt2:
    if i > 0:
        ttt2.append(i)

k2 -= mc
check = 0
ttt2.sort()
for i in ttt2:
    if k2 -i >= 0:
        k2 -= i
        maxs2 -= 2
        if i == tt2[-1] and check == 0:
            maxs2 += 1
            check = 1
    else:
        break

print(min(maxs, maxs2))

