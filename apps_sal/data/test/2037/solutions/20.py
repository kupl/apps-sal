

MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from collections import defaultdict as dd

n, m = I()
l = I()
d = dd(list)
for i in range(m):
	d[l[i]].append(i)

for i in d:
	d[i].sort()
ans = [0]*m
k = 1
# print(d)
index = 0
while True:
	for i in range(1, n + 1):
		if len(d[i]) < k:
			print(*ans, sep = '')
			return
		index = max(index, d[i][k-1])
	k += 1
	# print(index)
	ans[index] = 1
print(*ans, sep = '')
