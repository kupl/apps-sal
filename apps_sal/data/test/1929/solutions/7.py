n, t, c = list(map(int, input().split()))
seq = list(map(int, input().split()))

start, end = 0, 0
res = 0
for i in range(n):
	if seq[i] <= t:
		if end-start+1 == c:
			start += 1
			res += 1
		end += 1
	else:
		start, end = i, i

print(res)

