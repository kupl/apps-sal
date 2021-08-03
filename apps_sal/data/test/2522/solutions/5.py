from collections import Counter
from heapq import heapify, heappop, heappush
from itertools import groupby

n = int(input())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))

cnt_b = Counter(bbb)
hq_both = []
free_a = []
idx_a = {}
cnt_a = {}
i = 0
for a, itr in groupby(aaa):
    cnt = len(list(itr))
    idx_a[a] = i
    cnt_a[a] = cnt
    if a in cnt_b:
        cnt_ab = cnt + cnt_b[a]
        if cnt_ab > n:
            print('No')
            return
        hq_both.append((-cnt_ab, a))
    else:
        free_a.append(a)
    i += cnt
heapify(hq_both)

ans = [-1] * n
remaining = n

while hq_both:
    cnt_ab, b = heappop(hq_both)
    cnt_ab = -cnt_ab
    assert cnt_ab == cnt_a[b] + cnt_b[b]
    assert cnt_ab <= remaining

    cb = cnt_b[b]
    while cb:
        if hq_both:
            _, a = heappop(hq_both)
        else:
            a = free_a.pop()
        ca = cnt_a[a]

        fill_len = min(ca, cb)
        i = idx_a[a]
        ans[i:i + fill_len] = [b] * fill_len
        remaining -= fill_len
        idx_a[a] += fill_len
        cnt_a[a] -= fill_len
        cnt_b[b] -= fill_len
        cb -= fill_len

        if cnt_a[a] > 0:
            if a in cnt_b and cnt_b[a] > 0:
                heappush(hq_both, (-(cnt_a[a] + cnt_b[a]), a))
            else:
                free_a.append(a)

    free_a.append(b)

for b, cb in list(cnt_b.items()):
    if cb == 0:
        continue
    while cb:
        a = free_a.pop()
        ca = cnt_a[a]

        fill_len = min(ca, cb)
        i = idx_a[a]
        ans[i:i + fill_len] = [b] * fill_len
        idx_a[a] += fill_len
        cnt_a[a] -= fill_len
        cb -= fill_len

        if cnt_a[a] > 0:
            free_a.append(a)

print('Yes')
print((*ans))
