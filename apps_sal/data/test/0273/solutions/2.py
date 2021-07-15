s = input().split()
d = set()
for i in range(1, len(s[0]) + 1):
	for j in range(1, len(s[1]) + 1):
		d.add(s[0][:i] + s[1][:j])
print(sorted(d)[0])
