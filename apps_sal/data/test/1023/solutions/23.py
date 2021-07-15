n, m, ta, tb, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [i+ta for i in a]

i=0
j=0

ans = 0

for _k in range(k+1):
	dk = _k
	i=0
	if dk >= n:
		# all flights in a will be cancelled
		print(-1)
		return
	else:
		# dk flights from a has been cancelled
		key = a[dk]
		dk = k-_k
		while j<m and b[j]<key:
			j+=1
		# print("j", j)
		if j is m:
			print(-1)
			return
		else:
			if m<=dk+j:
				print(-1)
				return
			else:
				ans = max(ans, b[j+dk]+tb)
	# print("k {} | {} | {}".format(_k, a[dk+1], b[j+dk]))

print(ans)
