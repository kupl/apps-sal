n = int(input())
s = input().split()
ans = 0
for word in s:
	v = 0
	for q in word:
		if (q >= 'A' and q <= 'Z'):
			v += 1
	ans = max(ans, v)
print(ans)
