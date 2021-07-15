from bisect import *


n = int(input())
h = list(map(int,input().split()))
t = list(map(int,input().split()))

dp 		= [1 for i in range(n+1)]
reminder= [0 for i in range(n+1)]
pre_sum = [0 for i in range(n)]

pre_sum[0] = t[0]

for i in range(1,n):
	pre_sum[i] = pre_sum[i-1] + t[i]


pre = 0

for i in range(n):
	cur   = pre + h[i]
	pre   = pre_sum[i]
	index = bisect(pre_sum,cur)

	
	# try:
	# 	dp[index]-=1
	# except:
	# 	print(i,index,cur)
	dp[index]-=1
	if(index==0):
		reminder[index]+=cur
	else:
		reminder[index] += cur - pre_sum[index-1]
# 	print('index',index)
# 	print('dp',dp)
# 	print('reminder',reminder)

# print(*dp)
# print(*reminder)	


for i in range(1,n):
	dp[i] =dp[i-1]+dp[i]

for i in range(n):
	temp= dp[i]*t[i]+reminder[i]
	print(temp,end=' ')
print()






 
