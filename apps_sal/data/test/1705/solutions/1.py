n=int(input())
arr=list(map(int,input().split()))
count1=arr.count(0)
count2=arr.count(1)
ans1=0
ans2=0
for i in range(n):
	if(arr[i]==0):
		ans1+=1
	else:
		ans2+=1
	if(ans1==count1):
		print(i+1)
		return
	elif(ans2==count2):
		print(i+1)
		return

