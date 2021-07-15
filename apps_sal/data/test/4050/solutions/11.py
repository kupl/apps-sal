n=int(input())
arr=list(map(int,input().split()))
dict1={}
for i in range(n):
	val=0
	for j in range(i,n):
		val+=arr[j]
		try:
			dict1[val].append((i,j))
		except:
			KeyError
			dict1[val]=[(i,j)]
ans=0
ansarr=[]
for i in list(dict1.keys()):
	#print(i,len(dict1[i]))
	if(len(dict1[i])>ans):
		arr2=[]
		for j in range(len(dict1[i])):
			count=0
			for k in range(len(dict1[i])):
				if(dict1[i][k][0]<=dict1[i][j][0]<=dict1[i][k][1] or dict1[i][k][0]<=dict1[i][j][1]<=dict1[i][k][1]  or dict1[i][j][0]<=dict1[i][k][0]<=dict1[i][j][1]  or dict1[i][j][0]<=dict1[i][k][1]<=dict1[i][j][1]):
					count+=1
			arr2.append((count,j))
		arr2.sort()
		temp=[]
		for j in range(len(arr2)):
			flag=0
			indexi=dict1[i][arr2[j][1]][0]
			indexj=dict1[i][arr2[j][1]][1]
			for k in range(len(temp)):
				if(temp[k][0]<=indexi<=temp[k][1] or temp[k][0]<=indexj<=temp[k][1] or indexi<=temp[k][0]<=indexj or indexi<=temp[k][1]<=indexj):
					flag=1
			if(flag==0):
				temp.append((indexi,indexj))
		if(len(temp)>ans):
			ans=len(temp)
			ansarr=temp
print(ans)
finalans=[]
for i in range(len(ansarr)):
	finalans.append(ansarr[i][0]+1)
	finalans.append(ansarr[i][1]+1)
print(*finalans)



