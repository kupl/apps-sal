def ans(s):
	size = len(s)
	flag = True
	for i in range(1, size):
		if s[i-1] < s[i]:
			break
		if s[i-1] == s[i]:
			continue
		if s[i-1] > s[i]:
			flag = False
			break
	x = 0
	if flag:
		x = int(s[0])
	else:
		x = int(s[0])-1
	return x+(size-1)*9
for i in range(int(input())):
    print(ans(input()))

