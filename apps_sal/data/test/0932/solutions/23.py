n, k = [int(x) for x in input().split()]
arr = []
ans = []
rows = [0] * n
cols = [0] * k
for i in range(n):
	arr.append(input().split())
	ans.append(['0'] * k)
	rows[i] = all([a == '1' for a in arr[-1]])
for i in range(k):
	sum = 0
	for j in range(n):
		sum += 1 if arr[j][i] == '1' else 0
	if sum == n:
		cols[i] = True
for i in range(n):
	for j in range(k):
		if ((arr[i][j] == '1' and not rows[i] and not cols[j]) or
                   (arr[i][j] == '0' and (rows[i] or cols[j]))):
			print('NO')
			return
if any(rows) ^ any(cols):
	print('NO')
	return
for i in range(n):
	if not rows[i]:
		continue
	for j in range(k):
		if cols[j]:
			ans[i][j] = '1'
print('YES')
print('\n'.join(' '.join(l) for l in ans))

