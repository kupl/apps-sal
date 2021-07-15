n=int(input())
arr=list(map(int,input().split()))
dict1={}
for i in range(2*n):
	try:
		dict1[arr[i]].append(i+1)
		dict1[arr[i]].sort()
	except:
		KeyError
		dict1[arr[i]]=[i+1]
ans=0
curr1=1
curr2=1
for i in range(1,n+1):
	if(i==1):
		ans+=(dict1[i][0]-curr1)
		ans+=(dict1[i][1]-curr2)
		curr1=dict1[i][0]
		curr2=dict1[i][1]
	elif(dict1[i][0]>curr1 and dict1[i][0]>curr2):
		ans+=(dict1[i][0]-curr1)
		ans+=(dict1[i][1]-curr2)
		curr1=dict1[i][0]
		curr2=dict1[i][1]
	elif(dict1[i][1]<curr1<curr2):
		ans+=abs(dict1[i][0]-curr1)
		ans+=abs(dict1[i][1]-curr2)
		curr1=dict1[i][0]
		curr2=dict1[i][1]
	elif(dict1[i][0]<curr1 and curr1<dict1[i][1]<curr2):
		ans+=abs(dict1[i][0]-curr1)
		ans+=abs(dict1[i][1]-curr2)
		curr1=dict1[i][0]
		curr2=dict1[i][1]
	elif(dict1[i][0]<curr1 and dict1[i][1]<curr2):
		ans+=abs(dict1[i][0]-curr1)
		ans+=abs(dict1[i][1]-curr2)
		curr1=dict1[i][0]
		curr2=dict1[i][1]
	elif(curr1<dict1[i][0]<dict1[i][1]<curr2):
		ans+=abs(dict1[i][0]-curr1)
		ans+=abs(dict1[i][1]-curr2)
		curr1=dict1[i][0]
		curr2=dict1[i][1]
	else:
		ans+=abs(dict1[i][0]-curr1)
		ans+=abs(dict1[i][1]-curr2)
		curr1=dict1[i][0]
		curr2=dict1[i][1]
print(ans)


