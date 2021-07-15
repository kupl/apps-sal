n, c = list(map(int, input().split()))
a = [0]
a.extend([int(i) for i in input().split()])
cntc = [0]
seg = {}
last = {}
for i in range(1, n + 1):
	cntc.append(cntc[i - 1] + (1 if a[i] == c else 0))
def getcntc(left, right):
	# [left, right]
	return cntc[right] - cntc[left - 1]
for i in range(1, n + 1):
	# print(-getcntc(last.setdefault(a[i], 0) + 1, i - 1))
	seg.setdefault(a[i], []).append(-getcntc(last.setdefault(a[i], 0) + 1, i - 1))
	last[a[i]] = i
	seg[a[i]].append(1)
for key in seg:
	# print(key, last[key])
	seg[key].append(-getcntc(last[key] + 1, n))
total = 0
m = max(a)
for d in range(1, m + 1):
	peak = 0
	ans = 0
	if d in seg and d != c:
		# print(seg[d])
		for s in seg[d]:
			ans = max(0, ans + s)
			peak = max(ans, peak)
		peak += getcntc(1, n)
	total = max(total, peak)
total = max(total, getcntc(1, n))
print(total)



