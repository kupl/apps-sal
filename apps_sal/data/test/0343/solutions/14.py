3.4

v = input().split()
n, k, p, x, y = int(v[0]), int(v[1]), int(v[2]), int(v[3]), int(v[4])

if p < y:
	print('-1')
	return

b = list(map(int, input().split()))
b.sort()

cur = sum(b)

if cur+n-k > x:
	print(-1)
	return

median = (n+1) // 2

lower_bound = len(b)-1

while lower_bound >= 0 and b[lower_bound] >= y:
	lower_bound -= 1
lower_bound += 2

max_count_of_ones = median - lower_bound
if max_count_of_ones < 0:
	print(-1)
	return

if max_count_of_ones + y*(n-k-max_count_of_ones)+cur > x:
	print(-1)
	return

for i in range(min(n-k, max_count_of_ones)):
	print('1', end=' ')
for i in range(min(abs(n-k-max_count_of_ones), n-k-max_count_of_ones)):
	print(y, end=' ')

