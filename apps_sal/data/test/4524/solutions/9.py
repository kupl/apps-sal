import math
dict1={}
mod=998244353
for i in range(20):
	dict1[i]=0
n,m=list(map(int,input().split()))
s1=str(input())
s2=str(input())
count1=0
arr=[]
for i in range(len(s2)):
	if(s2[i]=='1'):
		count1+=1
	arr.append(count1)
j=len(s1)-1
k=min(len(s1),len(s2))
i=0
while(k>0):
	if(s1[j]=='1'):
		dict1[i]=arr[len(s2)-i-1]
	i+=1
	j-=1
	k-=1
ans=0
for i in dict1:
	if(dict1[i]>0):
		ans=((ans%mod)+(((dict1[i]%mod)*(pow(2,i,mod)%mod))%mod))%mod
print(ans)

