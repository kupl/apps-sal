l=[100,20,10,5,1]
count=0
n=int(input())
for i in l:
	count=count+n//i
	n=n%i
print (count)

