from operator import itemgetter


def bin_search(lo, hi, key):
    while (lo < hi):
        md = (hi + lo) // 2
        if (md >= key(md)):
            hi = md
            #print("new hi:", hi)
        else:
            lo = md + 1
            #print("new lo:", lo)
    return lo  # or hi, they're equal at this point


def key_func(budget, prices):
    for k in range(1 + budget // prices[2]):
        budget2 = budget - k * prices[2]
        for j in range(1 + budget2 // prices[1]):
            budget3 = budget2 - j * prices[1]
            i = budget3 // prices[0]
            if survive(i, j, k):
                return budget - 1
    return budget + 1


def survive(i, j, k):
    # nonlocal y, m, p, penumsorted
    toadd = [i, j, k]
    newy = list(y)
    newmhp = m[0]
    for i, item in enumerate(penumsorted):
        newy[item[0]] = y[item[0]] + toadd[i]
    # print(vars())
    while newy[0] > 0 and newmhp > 0:
        oldmhp = newmhp
        newy[0] -= max(0, m[1] - newy[2])
        newmhp -= max(0, newy[1] - m[2])
        if oldmhp == newmhp:
            newy[0] = 0
    if newmhp <= 0 and newy[0] > 0:
        return True
    else:
        return False


y = list(map(int, input().split()))
m = list(map(int, input().split()))
p = list(map(int, input().split()))
psorted = sorted(p)
penum = list(enumerate(p))
penumsorted = sorted(penum, key=itemgetter(1))
print(bin_search(0, 20000, lambda x: key_func(x, psorted)))
