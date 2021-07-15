import math
t = int(input())
for i in range(t):
	k = int(input())
	ans = k * (k + 1) // 2
	pw = 2 ** (math.floor(math.log2(k)) + 1) - 1
	print(ans - 2 * pw)
