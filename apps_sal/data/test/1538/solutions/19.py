n=int(input())
a=list(map(int,input().split()))
s=set(a)
ma=1
for i in s:
	k=a.count(i)
	if k > ma:
		ma=k
print(ma)
	

