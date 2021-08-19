from copy import copy
raw = [int(x) for x in input().split(' ')]
n = raw[0]
d = raw[1]
a = [int(x) for x in input().split(' ')]
a = sorted(a)
strat = 0
best = 200
going = True


def dimof(li):
    return li[-1] - li[0]


while strat < 101 and going:
    c = 0
    temp = a.copy()
    for i in range(strat):
        if dimof(temp) <= d:
            break
        del temp[0]
        c += 1
    if going:
        if dimof(temp) <= d:
            going = False
        else:
            while dimof(temp) > d:
                del temp[-1]
                c += 1
    if c < best:
        best = c
    strat += 1
print(best)
