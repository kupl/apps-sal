A, B = map(int, input().split())

i = A + 1
ans = 1

while i <= B:
	ans = ans * (i % 10)
	ans = ans % 10
	if (ans % 10) == 0:
		break
	i = i + 1

print(ans) 
