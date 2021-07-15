# ===================================
# (c) MidAndFeed aka ASilentVoice
# ===================================
# import math, fractions, collections
# ===================================
n, d = [int(x) for x in input().split()]
s = str(input())
i = 0
ans = 0
temp = 0
while(1):
	temp = min(d, n-i-1)
	
	while(temp > 0):
		if s[i+temp] == "1":
			flag = 1
			break
		else:
			temp -= 1

		if temp == 0:
			flag = 0

	ans += 1
	i += temp

	# print(i, ans)

	if i == n-1 or not(flag):
		break

if i+1 == n:
	print(ans)
else:
	print(-1)

