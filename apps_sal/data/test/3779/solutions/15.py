import math
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ddc = 0
f = 1
ans = set()
for x in a:
	if f:
		ddc = x%k
	o = 0
	o = x%k
	if not f:
		ddc = math.gcd(ddc, o)
	
	if o == 1:
		print(k)
		print(*list(range(k)))
		return
	f = 0
	'''
	if k%2 != o%2 and math.gcd(k, o)==1:
		print(k)
		
		print(*range(k))
		return
	
	if not o in ans:
		yy = o
		ans.add(o)
		while o != 0:
			o+=yy
			o%=k
			ans.add(o)
		ans.add(0)
	
a = list(sorted(ans))
for i in range(len(a)):
	for j in range(i , len(a)):
		ans.add((a[i]+a[j])%k)
'''
yy = ddc
while yy:
	ans.add(yy)
	yy+=ddc
	yy%=k
ans.add(0)
print(len(ans))
print(*(sorted(ans)))


