n = int(input())
s = input()
o = [0] * 10
for c in s:
	if c == 'L':
		for i in range(10):
			if not o[i]:
				o[i] = 1
				break
	elif c == 'R':
		for i in range(9, -1, -1):
			if not o[i]:
				o[i] = 1
				break
	else:
		o[ord(c) - ord('0')] = 0
print(''.join(map(str, o)))
