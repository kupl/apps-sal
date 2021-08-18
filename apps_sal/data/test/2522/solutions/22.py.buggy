from collections import Counter
from heapq import heapify, heappop, heappush
from itertools import groupby

n = int(input())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))

idx_a = {}
cnt_a = {}
i = 0
for a, itr in groupby(aaa):
    cnt = len(list(itr))
    idx_a[a] = i
    cnt_a[a] = cnt
    i += cnt

cnt_b = Counter(bbb)
hq_both = []
hq_free = []
for a, ca in list(cnt_a.items()):
    if a in cnt_b:
        hq_both.append((-(ca + cnt_b[a]), a))
    else:
        hq_free.append(a)
heapify(hq_both)

# Aの個数とBの個数の和が大きいやつがヤバげ

ans = [-1] * n
remaining = n

while hq_both:
    cab, a1 = heappop(hq_both)
    cab = -cab
    assert cab == cnt_a[a1] + cnt_b[a1]

    # print(a1, cab, cnt_a, cnt_b, ans, hq_both, hq_free)

    if cab > remaining:
        print('No')
        return

    cb = cnt_b[a1]
    while cb:
        if hq_both:
            _, a2 = heappop(hq_both)
            pop_from_que = True
        else:
            a2 = hq_free.pop()
            pop_from_que = False
        ca = cnt_a[a2]
        # print('b', cb, a2, pop_from_que, ca <= cb, hq_both, hq_free)
        if ca <= cb:
            l = idx_a[a2]
            ans[l:l + ca] = [a1] * ca
            remaining -= ca
            idx_a[a2] += ca
            cnt_a[a2] -= ca
            cnt_b[a1] -= ca
            cb -= ca
        else:
            l = idx_a[a2]
            ans[l:l + cb] = [a1] * cb
            remaining -= cb
            idx_a[a2] += cb
            cnt_a[a2] -= cb
            cnt_b[a1] -= cb
            cb = 0
            if pop_from_que:
                heappush(hq_both, (-(cnt_a[a2] + cnt_b[a2]), a2))
            else:
                hq_free.append(a2)
        # print('b', cb, a2, pop_from_que, ca <= cb, hq_both, hq_free)
    hq_free.append(a1)

for b, cb in list(cnt_b.items()):
    if cb == 0:
        continue
    while cb:
        a = hq_free.pop()
        ca = cnt_a[a]
        if ca <= cb:
            l = idx_a[a]
            ans[l:l + ca] = [b] * ca
            cb -= ca
        else:
            l = idx_a[a]
            ans[l:l + cb] = [b] * cb
            idx_a[a] += cb
            cnt_a[a] -= cb
            cb = 0
            hq_free.append(a)

print('Yes')
print((*ans))
