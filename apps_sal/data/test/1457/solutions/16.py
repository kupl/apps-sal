a=list(input())
b=list(input())
r=0
for i in range(len(a)-len(b)+1):
	if a[i:i+len(b)] == b:
		r+=1
		a[i+len(b)-1] = '#'
print(r)
