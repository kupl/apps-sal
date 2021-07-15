n,k=list(map(int ,input().split()))
h=list(map(int ,input().split()))
count=0
for i in range(0,len(h)):
	if(h[i] == k or h[i] >=k ):
		count+=1
	else:
		count+=0

print((int(count)))

