s = input()
(x, y) = map(int, input().split())
tInd = [i for (i, x) in enumerate(s) if x == 'T']
xs = []
ys = [0]
answer = 'No'
xa = False
firstT = False
if s[0] == 'T':
    firstT = True
start = 0
isx = 1
for i in tInd:
    if isx == 1:
        xs.append(i - start)
    else:
        ys.append(i - start)
    isx *= -1
    start = i + 1
if isx == 1:
    xs.append(len(s) - start)
else:
    ys.append(len(s) - start)
cset = {0}
for (index, item) in enumerate(xs):
    tcset = set()
    if index == 0 and (not firstT):
        tcset.add(item)
    else:
        for c in cset:
            tcset.add(c + item)
            tcset.add(c - item)
    cset = tcset
if x in cset:
    xa = True
if xa:
    cset = {0}
    for item in ys:
        tcset = set()
        for c in cset:
            tcset.add(c + item)
            tcset.add(c - item)
        cset = tcset
    if y in cset:
        answer = 'Yes'
print(answer)
