N,A = list(map(int,input().split()))
Y = list([int(x)-A for x in input().split()])
dp = {0:1}

for y in Y:
	for k,v in list(dp.items()):
		dp[k+y]=dp.get(k+y,0)+v

print((dp[0]-1))

