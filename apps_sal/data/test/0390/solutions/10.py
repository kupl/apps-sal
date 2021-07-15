
def mi():
	return map(int, input().split())

n,w,b = mi()
a = list(mi())


if w<b:
	mc = 0
else:
	mc = 1
ans = 0
c = [w,b]
for i in range(n//2):
	if a[i]==a[n-1-i]:
		if a[i]==2:
			ans+=2*min(w,b)
	if a[i]!=a[n-1-i]:
		if max(a[i],a[n-1-i])!=2:
			print (-1)
			return
		ans+=c[min(a[i],a[n-1-i])]
if a[n//2]==2 and n%2:
	ans+=min(w,b)
print (ans)
