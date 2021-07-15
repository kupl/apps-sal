def ceiling_div(x, y):
	res = x // y
	if (x % y != 0):
		res += 1
	return res
	
k, a, b, v = list(map(int, input().split()))
sec = ceiling_div(a, v)
res = max(sec - b, ceiling_div(sec, k))
print(res)

