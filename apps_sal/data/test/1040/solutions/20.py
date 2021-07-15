n = int(input())
t = input()
s = []
for i in range(n):
	s.append(t[i])
	if len(s) > 2 and s[-3:] == ["f", "o", "x"]:
		for _ in range(3):
			s.pop()
print(len(s))
