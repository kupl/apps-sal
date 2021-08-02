def rp():
    cs = list(map(int, input().split(' ')))
    cs = list(zip(cs[0::2], cs[1::2]))
    return cs


def dist(p1, p2):
    return len(set(p1).union(set(p2))) - 2


input()

ps = [rp(), rp()]

theyCan = True
myPos = set()

for ps1, ps2 in [ps, ps[::-1]]:
    for p1 in ps1:
        pos = set()

        for p2 in ps2:
            if dist(p1, p2) == 1:
                pos = pos.union(set(p1).intersection(set(p2)))

        if len(pos) >= 2:
            theyCan = False
        myPos = myPos.union(pos)

print(next(iter(myPos)) if len(myPos) == 1 else 0 if theyCan else -1)
