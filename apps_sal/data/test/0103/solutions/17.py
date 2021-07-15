n = int(input())
s = list(map(int, input().split()))
s = [0] + s[:] + [1001]
c = 0
maxc = 0
for i in range(1, len(s)):
	if s[i] - s[i - 1] == 1:
		c += 1
		if c > maxc:
			maxc = c-1
	else:
		c = 0
print(maxc)
