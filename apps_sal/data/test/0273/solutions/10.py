s, t = input().split()

l = []
for i in range(len(s)):
	for j in range(len(t)):
		l.append(s[:i+1] + t[:j+1])
l.sort()

print(l[0])

