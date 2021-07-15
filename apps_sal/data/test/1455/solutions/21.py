n = int(input())
if n%2:
	size = (n+1)//2
else:
	size = n//2+1
print(size)
for i in range(n):
	if i < size:
		print(1, i+1)
	else:
		print(i-size+2, size)
