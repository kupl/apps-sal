n = int(input())
whSumv = (n * (n+1)) // 2
sumv = 0
ans = []
for i in reversed(range(1, n+1)):
	if sumv + i <= whSumv//2:
		sumv += i
		ans += [i]
print(abs(whSumv-sumv-sumv))
print(len(ans), ' '.join(map(str, ans)))
