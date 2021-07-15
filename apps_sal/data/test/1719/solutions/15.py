mod=10**9+7
n=int(input())
dp=[[0]*64 for _ in range(n+1)]
dp[0][0]=1
#3前、2前,1前,今の文字
#t=0,a=1,g=2,c=3
ban_list=[]
for i in range(256):
	p=[i//64%4,i//16%4,i//4%4,i%4]
	if p[1:]==[1,2,3] or p[1:]==[1,3,2] or p[1:]==[2,1,3]\
	or (p[:2]==[1,2] and p[3]==3) or (p[0]==1 and p[2:]==[2,3]):
		ban_list.append(i)
for i in range(n):
	for j in range(4):
		for k in range(64):
			three=k*4%64+j
			four=k*4+j
			if four not in ban_list:
				dp[i+1][three]+=dp[i][k]
				dp[i+1][three]%=mod
ans=0
for x in dp[-1]:
	ans+=x
	ans%=mod
print(ans)
