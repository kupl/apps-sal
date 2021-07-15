n = int(input())
l = list(map(int,input().split()))
wyk = [0] * n
for i in range(n):
	left = 0
	right = 72
	while abs(left-right) > 1:
		mid = (left+right)//2
		if l[i] % (2**mid) == 0:
			left = mid
		else:
			right = mid
	mid = (left+right)//2
	if l[i] % (2**(mid+1)) == 0:
		wyk[i] = mid+1
	else:
		wyk[i] = mid
d = {}
for i in wyk:
	d[i] = 0
for i in wyk:
	d[i] += 1
mak = -888999
faw = 0
for i in d:
	if d[i] >= mak:
		mak = d[i]
		faw = i
print(n - mak)
for i in range(n):
	if wyk[i] != faw:
		print(l[i])

