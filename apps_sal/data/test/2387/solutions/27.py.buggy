N = int(input())
S = [input() for i in range(N)]

pos = []
neg = []
for s in S:
    sm = 0
    mn = 0
    for c in s:
        if c == '(':
            sm += 1
        else:
            sm -= 1
            mn = min(mn, sm)
    if sm >= 0:
        pos.append((mn, sm))
    else:
        neg.append((mn - sm, -sm))

pos.sort(key=lambda x: -x[0])
neg.sort(key=lambda x: -x[0])

hp = 0
for m, s in pos:
    if hp + m < 0:
        print('No')
        return
    hp += s

hn = 0
for m, s in neg:
    if hn + m < 0:
        print('No')
        return
    hn += s

print('Yes' if hp == hn else 'No')
