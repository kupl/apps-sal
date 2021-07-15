nextInt = lambda: list(map(int, input().split()))
n,p=nextInt()
a=[0]*n
ret=0
for i in range(n):
    l,r=nextInt()
    a[i]=(r//p-(l-1)//p)/(r-l+1)

for i in range(n):
    ret+=a[i]+a[i-1]-a[i]*a[i-1]

# print(a)

ret*=2000

print(ret)

