import sys
input=sys.stdin.readline

n,m,d=list(map(int,input().split())) 
arr=list(map(int,input().split())) 
tot=sum(arr)
res=[0]*n
gap=1
ptr=0
j=0
bool1=True
while(j<n):
	if(gap<d and n-(j+1)>=tot):
		j+=1
		gap+=1
		continue
	else:
		if(ptr<m):
			for k in range(j,j+arr[ptr]):
				res[k]=(ptr+1)
			gap=1
			tot-=arr[ptr]
			j+=arr[ptr]
			# print(j-1)
			ptr+=1
		else:
			j+=1
			bool1=False
	# print(j)
# print(res,bool1)
if(bool1==False):
	print("NO")	
else:
	print("YES")
	s=""
	for i in res:
		s=s+str(i)+" "
	s=s[:-1]
	print(s)



