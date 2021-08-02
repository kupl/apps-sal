import sys
from operator import itemgetter


def input():
    return sys.stdin.readline().strip()


n, m = list(map(int, input().split()))

trees = set(map(int, input().split()))
occ = set(trees)
newadd = set()
for x in trees:
    if x + 1 not in occ:
        newadd.add((x + 1, 1))
    if x - 1 not in occ:
        newadd.add((x - 1, 1))

anspos = []
ans = 0
while m > 0:
    newnewadd = set()
    while m > 0 and len(newadd) > 0:
        x, diff = newadd.pop()
        if x in occ:
            continue
        occ.add(x)
        anspos.append(x)
        ans += diff
        if x + 1 not in occ:
            newnewadd.add((x + 1, diff + 1))
        if x - 1 not in occ:
            newnewadd.add((x - 1, diff + 1))
        m -= 1
    newadd = newnewadd
print(ans)
print(*anspos)
