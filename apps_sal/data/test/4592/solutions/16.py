prime = [False] * 1001

for i in range(2,1001):
	if prime[i] == False:
		for j in range(i*i,1001,i):
			prime[j]=True

n = int(input())

cnt = [0] * 1001
for i in range(2,n+1):
	for j in range(2,n+1):
		if prime[j] == False:
			val = i
			while val%j==0:
				cnt[j]+=1
				val/=j

ans=1

for x in cnt:
	ans*=(x+1)
	ans%=1000000007

print(ans)
