n = int(input())
a = list(map(int,input().split()))
a.sort()

dp = [0]*a[-1]
for x in a:
	if dp[x-1] == 0:
		y = 2*x
		while y <= a[-1]:
			dp[y-1] = 1
			y += x

sum = 0
d = [0]*a[-1]
for i in a:
	if dp[i-1] == 0:
		d[i-1] += 1
for i in a:
	if d[i-1] == 1:
		sum += 1
print(sum)
