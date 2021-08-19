import numpy as np
(n, k) = map(int, input().split())
a = np.array(list(map(int, input().split())))
a.sort()
pos = a[a > 0]
zero = a[a == 0]
neg = a[a < 0]
negpos = (neg * -1)[::-1]
lenn = len(neg)
lenz = len(zero)
lenp = len(pos)
nnres = lenn * lenp
nzres = int(lenz * (lenn + lenp) + lenz * (lenz - 1) / 2)
npres = int(lenn * (lenn - 1) / 2 + lenp * (lenp - 1) / 2)
if k <= nnres:

    def count_nnres(x):
        cnt = np.searchsorted(neg, x // pos, side='right').sum()
        return int(cnt)
    left = -10 ** 18
    right = -1
    while left + 1 < right:
        mid = (left + right) // 2
        nebefore = count_nnres(mid)
        if nebefore >= k:
            right = mid
        elif nebefore < k:
            left = mid
    print(right)
elif nnres < k <= nnres + nzres:
    print(0)
elif nnres + nzres < k:

    def count_npres(x):
        cnt = 0
        cnt += int(np.searchsorted(pos, x // pos, side='right').sum() - (x // pos >= pos).sum()) // 2
        cnt += int(np.searchsorted(negpos, x // negpos, side='right').sum() - (x // negpos >= negpos).sum()) // 2
        return cnt
    k -= nnres + nzres
    left = 1
    right = 10 ** 18
    while left + 1 < right:
        mid = (left + right) // 2
        nebefore = count_npres(mid)
        if nebefore >= k:
            right = mid
        elif nebefore < k:
            left = mid
    print(right)
