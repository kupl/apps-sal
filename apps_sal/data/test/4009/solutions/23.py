l=(input().split())
n=int(l[0])
x=int(l[1])
y=int(l[2])
num=input()
count=0
for i in range(n-1,n-x-1,-1):
	if i==(n-1-y):
		if num[i]=="0":
			count+=1
	else:
		if num[i]=="1":
			count+=1
print (count)
