k = int(input())
s = ""
i = 1
while len(s) < k + 10:
	s += str(i)
	i += 1
k -= 1
print(s[k])
