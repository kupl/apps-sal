input()
B = 10000
s = [0, B, B]
for x in map(int, input().split()):
	s = [min(s) + 1, min(s[0::2]) if x & 1 else B, min(s[:2]) if x & 2 else B]
print(min(s))

