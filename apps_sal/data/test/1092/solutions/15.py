M= 1000000007
f = [1]*2000
for i in range(1,2000):
    f[i]=f[i-1]*i%M
n,m = list(map(int,input().split()))
a = sorted(map(int,input().split()))
b = []
for i in range (1,m):
    x=a[i]-a[i-1]-1
    if(x>0):
        b.append(x)
#print(b)
count = pow(2,sum(b)-len(b),M)*f[n-m]%M
#print(count)
b = [a[0]-1]+b+[n-a[-1]]
#print(b)
#print(f[3])
for i in b:
	count = count*pow(f[i],M-2,M)%M
	#print(pow(f[i],M-2,M))
	#print(i)
print(count)

