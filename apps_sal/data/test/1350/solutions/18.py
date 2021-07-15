n,k=list(map(int,input().split()))
s=input()
a=[0]*26
for i in s:
	a[ord(i)-ord('A')]+=1
ans=100000000
for i in range(k):
	ans=min(ans,a[i])
print(ans*k)

