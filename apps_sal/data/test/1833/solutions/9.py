#multiplicity
n=int(input())
a=[int(x) for x in input().split()]

hell=10**9+7
dp=[0]*(n+5)
dp[0]=1
import math
for i,x in enumerate(a):
	
	j=1
	t_dp={}
	while j<=min(i+1,int(math.sqrt(x))):
		
		if(x%j == 0):
			t_dp[j]=(dp[j]+dp[j-1])%hell
			if(x//j != j and x//j <=(i+1)):
				t_dp[x//j]=(dp[x//j] + dp[ (x//j) -1])%hell
			
		j+=1
	
	for e in list(t_dp.keys()):
		dp[e]=t_dp[e]
	

ans=0
for i in dp[1:]:
    ans =(ans+ i)%hell
print(ans%hell)




