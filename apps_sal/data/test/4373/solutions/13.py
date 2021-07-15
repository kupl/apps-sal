n=int(input())
l=list(map(int,input().split()))
l.sort()
count=0
for i in l:
	if i>count:
		count+=1
print (count)
