n = int(input())
ans = 0
prev = 0
N = n
while n:
	a = n%10
	n //= 10
	ans += 1
	prev = a
if ans==1:
	print(1)
else:
	print(((prev+1)*(10**(ans-1)))-N)

