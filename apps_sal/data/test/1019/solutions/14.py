def g(a,b):
	if(b>a):
		return g(b,a)
	if(b== 0 ):
		return a
	return g(b,a%b)

n = int(input())
if(n%2 == 1):
	a = n//2
	b = n-n//2
else:
	a = n-n//2 - 1
	b = n-n//2 + 1
while(g(b,a) > 1):
	a -= 1
	b += 1
print(a,b)
