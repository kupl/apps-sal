n,x,y=map(int,input().split())
arr=list(map(int,input().split()))
if x<=y:
	c=0
	arr=sorted(arr)
	for i in range(0,len(arr),2):
		if arr[i]<=x:
			c+=1
	print(c)
	return
# if x==y:
# 	c=0
# 	for i in range(0,len(arr)):
# 		if arr[i]<=x:
# 			c+=1
# 	print(c//2)
# 	return
if x>y:
	c=0
	print(n)
