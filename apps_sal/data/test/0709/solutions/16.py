a = int(input())
ans = 0
while(a != 0):
	j = 0
	while(a % 2 == 0):
		j = 1
		a //= 2
	if (j == 0):
		ans += 1
		a -= 1
print(ans)
