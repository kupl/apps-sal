
def mi():
	return map(int, input().split())

n,k = mi()

t = 2*k+1
first = (t+1)//2
out = []
while first<=n:
	out.append(first)
	first+=t
if out==[]:
	out = [n]
if len(out) and (out[-1]+k<n):
	out.append(n)

if len(out)>1 and out[-1]-k<=out[-2]+k:
	diff = (out[-2]+k)-(out[-1]-k)+1
	if diff:
		for i in range(len(out)-1):
			out[i]-=diff
print (len(out))
print (*out)
