p = 10**9+7
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 1
for i in range(n//k):
	cnt = (10**k-1)//a[i] - (10**(k-1)*(b[i]+1)-1)//a[i]
	if b[i] != 0:
		cnt += (10**(k-1)*b[i]-1)//a[i] + 1
	ans = ans * cnt % p
print (ans)
