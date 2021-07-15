nearest_prime=[0]*(int(1e5+1))
nearest_prime[0]=2
nearest_prime[1]=1
prime_bool=[0]*(int(1e5+1))

def is_prime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

a=[]

for i in range(2,int(1e5)+1):
	if is_prime(i):
		a.append(i)
		prime_bool[i]=1

for i in range(100001,1000001):
	if is_prime(i):
		a.append(i)
		break

np=a[-1]
for i in range(int(1e5),1,-1):
	if prime_bool[i]:
		nearest_prime[i]=0
		np=i
	else:
		nearest_prime[i]=np-i

#print(nearest_prime[:10])

ans=1e9
n,m=list(map(int,input().split()))
arr=[]
for i in range(n):
	arr.append(list(map(int,input().split())))

for i in range(n):
	req=0
	for j in range(m):
		req+=nearest_prime[arr[i][j]]
#	print("row",i,req)
	ans=min(ans,req)

for i in range(m):
	req=0
	for j in range(n):
		req+=nearest_prime[arr[j][i]]
#	print("col",i,req)
	ans=min(ans,req)

print(ans)

