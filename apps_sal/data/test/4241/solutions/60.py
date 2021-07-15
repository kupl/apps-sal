s,t=input(),input()
ans = len(t)
for i in range(len(s)-len(t)+1):
	s2 = s[i:i+len(t)]
	c = 0
	for j in range(len(s2)):
		if (s2[j] != t[j]):
			c += 1
	ans = min(ans, c)
print(ans)
