import sys

n, m = [int(x) for x in input().split(' ')]
arr = [int(x)-1 for x in input().split(' ')]
k = [int(x) for x in input().split(' ')]

summ = 0
for i in range(m):
	summ += k[i]

for i in range(n):
	if i >= summ:
		k[arr[i-summ]] += 1
	k[arr[i]] -= 1
	done = True
	for j in range(m):
		if k[j] != 0:
			done = False
	if done:
		print('YES')
		return
print('NO')
