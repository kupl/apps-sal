n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
i = 0
c = 0
x = 0
y = 0 
while i < len(a) - 1:
	if a[i] == a[i+1] and c == 0:
		x = a[i]
		i += 2
		c += 1
		continue
	if a[i] == a[i+1] and c == 1:
		y = a[i]
		break
	i += 1
if x != 0 and y != 0:
	print(x*y)
else:
	print(0)
