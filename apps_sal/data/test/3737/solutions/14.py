n=int(input())
l=list(map(int,input().split()))
mi=min(l)
ma=max(l)
count=0
for i in l:
	if(i!=mi and i!=ma):
		count+=1
print(count)
