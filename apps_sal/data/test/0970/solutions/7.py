n=int(input())
arr=list(map(int,input().split()))
arr.sort()
sum1=0
j=1
k=2
sum2=0
for i in range(len(arr)):
	sum1+=abs(j-arr[i])
	sum2+=abs(k-arr[i])
	j+=2
	k+=2
print(min(sum1,sum2))

