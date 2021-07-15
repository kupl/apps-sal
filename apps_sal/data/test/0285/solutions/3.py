n=int(input())
l,r=list(map(int,input().split()))
i=0
s=[]
while i<n:
	k,b=list(map(int,input().split()))
	s.append([l*k+b,r*k+b])
	i+=1
s.sort()

y=0
i=1
while i<n:
	if s[i-1][1]>s[i][1]:y=1
	i+=1
print(["NO","YES"][y])

