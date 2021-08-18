from itertools import product
import copy


def trans(l):
    return [list(x) for x in list(zip(*l))]


h, w, k = map(int, input().split())
c = []
for _ in range(h):
    c.append([c for c in input()])

A = [i for i in product([1, 0], repeat=h)]
B = [i for i in product([1, 0], repeat=w)]

ans = 0
for a in A:
    temp1 = copy.copy(c)
    for i, x in enumerate(a):
        if x == 1:
            temp1[i] = ["."] * w
    for b in B:
        temp2 = trans(temp1)
        for i, x in enumerate(b):
            if x == 1:
                temp2[i] = ["."] * h

        cnt = 0
        for t in temp2:
            cnt += t.count("
        if cnt == k:
            ans += 1

print(ans)
