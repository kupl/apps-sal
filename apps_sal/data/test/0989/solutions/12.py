from collections import defaultdict
from itertools import accumulate
from bisect import bisect_left

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = defaultdict(int)

for u in a:
	d[u] += 1

c = sorted(d.keys())

cnt = [d[i] for i in c]
snt = [i * d[i] for i in c]

pc = list(accumulate(cnt))
sc = list(accumulate(cnt[::-1]))[::-1]

ps = list(accumulate(snt))
ss = list(accumulate(snt[::-1]))[::-1]

def get_high(rest):
	l, r = c[0] - 1, c[-1]
	while r - l > 1:
		mid = (l + r) // 2 + (l + r) % 2
		i = bisect_left(c, mid)
		if ss[i] - mid * sc[i] <= rest:
			r = mid
		else:
			l = mid
	return r

def calc_ans(low):
	if low < c[0]:
		return 10 ** 100
	i = bisect_left(c, low)
	if c[i] != low:
		i -= 1
	if low * pc[i] - ps[i] > k:
		return 10 ** 100
	rest = k - (low * pc[i] - ps[i])
	high = get_high(rest)
	return max(high - low, 0)

l, r = c[0], c[-1]

while r - l > 1:
	mid = (l + r) // 2
	mm = (mid + r) // 2
	if calc_ans(mid) <= calc_ans(mm):
		r = mm
	else:
		l = mid

print(min(calc_ans(l), calc_ans(r)))

