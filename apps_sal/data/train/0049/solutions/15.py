from itertools import combinations

all_classy = []


def all_possible(a):
    if len(a) == 0:
        return [['0'] * 19]
    lower = all_possible(a[1:])
    ans = []
    for l in lower:
        for x in range(1, 10):
            this = l[:]
            this[a[0]] = str(x)
            ans.append(this)
    return ans


for i in range(1, 4):
    for a in combinations(range(19), i):
        this_possible = all_possible(a)
        this_possible = [int(''.join(x)) for x in this_possible]
        all_classy += this_possible

all_classy.sort()


def ge(num):
    if num == 1:
        return 0
    lower, upper = 0, len(all_classy)
    while lower < upper - 1:
        mid = (lower + upper) >> 1
        if(all_classy[mid] < num):
            lower = mid
        else:
            upper = mid

    return upper


def le(num):
    lower, upper = 0, len(all_classy)
    while lower < upper - 1:
        mid = (lower + upper) >> 1
        if all_classy[mid] > num:
            upper = mid
        else:
            lower = mid

    return lower


q = int(input())

for i in range(q):
    l, r = map(int, input().strip().split())
    x, y = ge(l), le(r)
    print(y - x + 1)
