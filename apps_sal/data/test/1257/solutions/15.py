n, k = (int(x) for x in input().split())
summ = 0
data = []
for i in range(1, n+1):
	last = n**2-(n-k)*i -i+1
	data.append(last)
	summ += last
print(summ)
for i in range(1,n+1):
	t = list(range(last - k+1, last))
	value = [0]*n
	for j in range(1, n+1):
		if (j < k):
			value[j-1] = str((t[j-1]))
		elif (j == k):
			value[j-1] = str(data[i-1])
		else:
			value[j-1] = str(data[i-1] +j-k)
	last-=k-1
	print(' '.join(value))
