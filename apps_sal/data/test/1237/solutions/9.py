s, n = [int(i) for i in input().split()]
out = 0
for j in range(s):
	a, b = [int(i) for i in input().split()]
	out+=(n-a)
	out=max(out, b)
	n = a
out +=n
print(out)
	

