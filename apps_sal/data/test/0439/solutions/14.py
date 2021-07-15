n = int(input())
m = int(input())
cur = 1;
for i in range(n):
	cur *= 2
	if (cur > m):
		break
print(m % cur)
