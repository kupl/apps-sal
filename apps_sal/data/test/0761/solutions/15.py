
def mi():
	return map(int, input().split())

n = int(input())
a = list(mi())

cp,cn=0,0
for i in a:
	if i>=0:
		cp+=1
	if i<=0:
		cn+=1
s = 0 
if n==1:
	print (a[0])
	return
for i in a:
	s+=abs(i)
if cn and cp:
	print (s)
else:
	m = -1e100
	for i in a:
		m = max(m,s-2*abs(i))
	print (m)
