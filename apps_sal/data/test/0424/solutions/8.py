x2 = int(input())

s = [-1] * (x2 + 1)
for i in range(2, x2+1):
	if s[i] == -1:
		for j in range(i, x2+1, i):
			s[j] = i
	
ans = x2
for x1 in range(x2 - s[x2] + 1, x2 + 1):
	x0 = x1 - s[x1] + 1
	if x0 > 1:
		ans = min(ans, x0)

print(ans)

