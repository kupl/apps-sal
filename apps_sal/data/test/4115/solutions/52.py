a = list(input())
b = a[::-1]
count = 0
for i in range(len(a)):
	if a[i]!=b[i]:
		count += 1
		
print(count//2)
