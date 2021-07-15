n, m = list(map(int, input().split()))
ld, lh = list(map(int, input().split()))
mh = lh + (ld - 1) # 1-indexed
for i in range(1, m):
	d, h = list(map(int, input().split()))
	if abs(h - lh) > (d - ld):
		print('IMPOSSIBLE')
		return
	mh = max(mh, max(h, lh) + ((d - ld) - abs(h - lh)) // 2)
	ld, lh = d, h
mh = max(mh, lh + (n - ld))
print(mh) 

