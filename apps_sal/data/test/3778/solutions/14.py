n = int(input())
a = list(map(int, input().split()))

twos = []
threes = []
pts = []
for i, q in enumerate(a):
    i = i + 1
    if q == 0:
        # no targets
        pass
    elif q == 1:
        if twos:
            pts += [(twos.pop(), i)]
        elif threes:
            pts += [(threes.pop(), i), (i, i)]
        else:
            pts += [(i, i)]
    elif q == 2:
        pts += [(i, i)]
        if threes:
            pts += [(threes.pop(), i)]
        twos += [i]
    elif q == 3:
        pts += [(i, i)]
        if threes:
            pts += [(threes.pop(), i)]
        threes += [i]

if not twos and not threes:
    print(len(pts))
    for x in pts:
        print(*x)
else:
    print(-1)
