MOD = 10**9+7
n = int(input())
aa = input()
ab = input()
ba = input()
bb = input()

if ab == "A" and aa == "A":
	print(1)
elif ab == "B" and bb == "B":
	print(1)
elif ab == "A" and aa == "B":
	if ba == "B":
		print(pow(2, max(n-3, 0), MOD))
	else:
		res = [1, 1]
		for _ in range(max(n-3, 0)):
			res.append((res[-1] + res[-2]) % MOD)
		print(res[-1])
else:
	if ba == "A":
		print(pow(2, max(n-3, 0), MOD))
	else:
		res = [1, 1]
		for _ in range(max(n-3, 0)):
			res.append((res[-1] + res[-2]) % MOD)
		print(res[-1])
