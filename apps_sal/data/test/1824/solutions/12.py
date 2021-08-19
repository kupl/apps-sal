n = int(input())
inStr = input()
d0 = {}
for e in inStr.split():
    en = int(e)
    if not en in d0:
        d0[int(e)] = 0
    else:
        d0[int(e)] = d0[int(e)] + 1
inStr = input()
d1 = {}
for e in inStr.split():
    en = int(e)
    if not en in d1:
        d1[int(e)] = 0
    else:
        d1[int(e)] = d1[int(e)] + 1
inStr = input()
d2 = {}
for e in inStr.split():
    en = int(e)
    if not en in d2:
        d2[int(e)] = 0
    else:
        d2[int(e)] = d2[int(e)] + 1
ans0 = -1
for en in d0:
    if not en in d1 or not d0[en] == d1[en]:
        ans0 = en
        break
ans1 = -1
for en in d1:
    if not en in d2 or not d1[en] == d2[en]:
        ans1 = en
        break
print(ans0)
print(ans1)
