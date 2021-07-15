T = int(input())
s = input()
mid = len(s) // 2
MIN = -1

if len(s) < 3:
	print(int(s[0]) + int(s[1]))
	return

for i in range(mid, -1, -1):
	if s[i+1] != '0':
		MIN = int(s[:i+1]) + int(s[i+1:])
		break

for i in range(mid, len(s)):
	if s[i] != '0':
		tmp = int(s[:i]) + int(s[i:])
		if MIN > tmp:
			MIN = tmp
		break

if MIN == -1:
	MIN = int(s[:len(s)-1]) + int(s[len(s)-1:])

print(MIN)
