a=list(map(int,input().split()))
n=a[0]
x=a[1]

gg=list(map(int,input().split()))
gg.sort()
h=0
for i in range(n):
	h+=gg[i]*x
	if x>1: x-=1
print(h)

