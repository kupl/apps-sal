n = int(input())
n = n-1
x = int(n**0.5)
flag = True
for i in range(1, x+1):
	if(n%i==0):
		temp = n//i
		temp = temp - i - 1
		if(temp==0):
			continue
		if(temp%2==0):
			a = i
			b = temp//2
			flag = False
			break
if(flag):
	print("NO")
else:
	print(a,b)

