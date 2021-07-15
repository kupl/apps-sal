import sys
input = sys.stdin.readline

def bs(num):
	low=0
	high=len(rows)-1
	while low<high:
		mid=(low+high)//2
		if rows[mid]>=num:
			high=mid-1
		else:
			low=mid+1
	if rows[low]<num:
		return len(rows)-(low+1)
	else:
		return len(rows)-low

n,m=list(map(int,input().split()))
if n==0 and m==0:
	print(0)
	return
col=[]
rows=[]
for i in range(n):
	col.append(int(input()))
col.append(10**9)
for i in range(m):
	temp = list(map(int,input().split()))
	if temp[0]==1:
		rows.append(temp[1])
col.sort()
rows.sort()
ans=10**9
if len(rows)==0:
	print(0)
	return
for i in range(n+1):
	count1 = bs(col[i])
	ans=min(ans,count1+i)
print (ans)




