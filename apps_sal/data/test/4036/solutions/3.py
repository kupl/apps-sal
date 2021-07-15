kk=lambda:map(int,input().split())
# k2=lambda:map(lambda x:int(x)-1, input().split())
ll=lambda:list(kk())
n,k =kk()
su = ((k+1)*k)//2
start = (n-su)//k + 1
if n < su or n > start*((2**k)-1):
	print("NO")
	return
ls = [start+i for i in range(k)]
currsum = (start-1)*k+su
delayed = 0
for i in range(1, k):
	ls[i]+=delayed
	while ls[i-1]*2 > ls[i] and k-i <= n - currsum:
		delayed+=1
		ls[i]+=1
		currsum+= (k-i)
print("YES")
print(*ls)
