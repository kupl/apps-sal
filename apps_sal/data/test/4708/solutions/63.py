n=int(input())
k=int(input())
x=int(input())
y=int(input())
fees=0
if(k>n or n==k):
	for i in range(0,n):
		fees+=x
elif(k<n):
	diff=n-k
	for j in range(0,k):
		fees+=x
	for k in range(0,diff):
		fees+=y
		
print(fees)

