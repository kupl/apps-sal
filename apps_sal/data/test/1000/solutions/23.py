n, m = map(int,input().split())
base = min(n-1,m)
tt = (n-1)-m
i=2
while tt>0:
	base += i
	i += 1
	tt -= 1
print(base)
