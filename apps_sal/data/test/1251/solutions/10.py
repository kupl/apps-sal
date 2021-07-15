n = int(input())
t = [int(x) for x in input().split()]
t.insert(0, -1)

dp = [0] * (n+3)
dp[1] = t[1]

for i in range(2, n+1):
	#albo wszystkie na lewo sa pionowe
	dp[i] = t[i] + (i-1)
	#albo na lewo jest jakis poziomy
	smallest = t[i] #najmniejszy napotkany
	for j in range(i-1, 0, -1):
		#zakladam ze j jest ostatnim poziomym
		smallest = min(smallest, t[j])
		tmp = (dp[j] + (i-j-1) + (t[i] - smallest))
		dp[i] = min(dp[i], tmp)

res = n #kiedy wszystkie sa pionowe
for i in range(1, n+1):
	#i-ty jest ostanim poziomym
	res = min(res, dp[i] + (n-i))
print(res) 

