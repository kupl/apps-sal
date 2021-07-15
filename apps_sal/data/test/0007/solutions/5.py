import sys
n,m=input().split()
n=int(n);m=int(m)
ans=m
if m>=n:
	print(n)
	return
high=10**20;low=1
dif=n-m
#print("dif",dif)
while high-low>5:
	mid=high+low>>1
	if (1+mid)*mid>>1>=dif:
		high=mid
	else:
		low=mid
mid=max(0,mid-10)
while (1+mid)*mid>>1<dif:mid+=1
#print('mid',mid)
ans+=mid
print(ans)
