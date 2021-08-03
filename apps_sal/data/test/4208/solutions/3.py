n = int(input())

l = input()
r = input()

l = sorted(enumerate(l), key=lambda x: x[1])
l_ = []
lq = []
for pos, c in l:
    if c == "?":
        lq.append(pos)
    else:
        l_.append((pos, c))

r = sorted(enumerate(r), key=lambda x: x[1])
r_ = []
rq = []
for pos, c in r:
    if c == "?":
        rq.append(pos)
    else:
        r_.append((pos, c))


pairs = []
i = j = 0
while i < len(l_) and j < len(r_):
    posl, cl = l_[i]
    posr, cr = r_[j]

    if cl == cr:
        pairs.append((posl, posr))
        i += 1
        j += 1
    elif cl < cr:
        if rq:
            pairs.append((posl, rq.pop(0)))
        i += 1
    else:
        if lq:
            pairs.append((lq.pop(0), posr))
        j += 1

while i < len(l_) and rq:
    posl, cl = l_[i]
    pairs.append((posl, rq.pop(0)))
    i += 1

while j < len(r_) and lq:
    posr, cr = r_[j]
    pairs.append((lq.pop(0), posr))
    j += 1

for posl, posr in zip(lq, rq):
    pairs.append((posl, posr))

print(len(pairs))
for posl, posr in pairs:
    print(posl + 1, posr + 1)
