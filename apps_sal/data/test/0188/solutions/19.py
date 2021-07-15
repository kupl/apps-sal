n,k = list(map(int, input().split()))

a = list(map(int,input().split()))
all_sum = sum(a)
r4,r2 = n,n*2
for v in range(len(a)):
	mid = a[v] // 4
	a[v] = a[v] % 4
	if mid <= r4:
		r4 -= mid
	else:
		a[v] += 4 * (mid - r4)
		r4 = 0
	if r4 == 0:
		break
mid = 0
r22 = 0
for v in a:
	if v % 2 == 1:
		mid += 1
	r22 += v // 2
#print(r4,r22,mid,r2)
if r4 > 0:
	mid -=r4
	r22 -= r4
	if mid < 0:
		r22 -= (mid // -2)
		mid = 0

if r22 + mid > r2:
	print('NO')
else:
	print('YES')






