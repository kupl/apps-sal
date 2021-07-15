a=list(map(int,input().split()))
n=int(input())
s=list(map(int,input().split()))
b=[]
for i in range(n):
	for j in a:
		b.append((s[i]-j)*n+i)
b.sort()
cs={}
i=j=0
ans=10**18
def dd(w):
	cs[w]=cs.get(w,0)+1
def em(w):
	cs[w]-=1
	if cs[w]==0:cs.pop(w)
dd(b[0]%n)
while j<len(b):
	while j+1<len(b) and len(cs)<n:
		j+=1
		dd(b[j]%n)
	while len(cs)==n:
		ans=min(ans,b[j]//n-b[i]//n)
		em(b[i]%n)
		i+=1
	if j+1==len(b):
		break
print(ans)
