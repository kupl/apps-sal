n=int(input())
arr=list(map(int,input().split()))
count1=0
count2=0
count3=0
for i in range(n):
	if(arr[i]==0):
		count1+=1
	elif(arr[i]>0):
		count2+=1
	else:
		count3+=1
if(count2>=count1+count3):
	print(1)
elif(count3>=count1+count2):
	print(-1)
else:
	print(0)

