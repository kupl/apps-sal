def prost(a, b):
	a, b = max(a, b), min(a,b)
	while b!=0:
		a = a%b
		a, b = b, a
	if a==1:
		return (0)
	else:
		return (1)

n = int(input())
s = input().split()
k = 0
for i in range(len(s)-1):
	if prost(int(s[i]), int(s[i+1]))==1: 
		s[i] = s[i] + ' ' + '1'
		k = k+1
print (k)
print (' '.join(x for x in s))
