n,k = list(map(int,input().split()))
x = list(map(int,input().split()))

def f(a):
	return (a/10 + 1 - a/10.0)

x = sorted(x)
x = sorted(x,key = lambda a: (int(a/10) + 1 - a/10.0))
improved,i,flag = 0,0,0

while k>0:
	if i==n or x[i]==100:
		break
	if (int(x[i]/10) + 1 - x[i]/10.0)*10 > k:
		x[i]+=k
		k=0
		break
	k -= (int(x[i]/10) + 1 - x[i]/10.0)*10
	x[i] += (int(x[i]/10) + 1 - x[i]/10.0)*10
	i+=1
i=0
while k>0:
	if i==n:
		break
	if x[i]+k <= 100:
		x[i]+=k
		k=0
		break
	k-=100-x[i]
	x[i]=100
	i+=1
for i in range(0,n):
	improved+=int(x[i]/10)
print(improved)

