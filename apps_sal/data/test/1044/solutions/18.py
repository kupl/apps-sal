n=int(input())
a = list(map(int,input().split()))
odd,even=0,0
for i in range(n):
	if((a[i] & 1) and a[i]>1):
		odd+=1
	elif(not(a[i] & 1) and a[i]>1):
		even+=1
	if((even & 1)):
		print("1")
	else:
		print("2")
