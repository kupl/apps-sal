def check(s, dep):
	if len(s) == 0:
		return True;
	flag = False
	if s[-1:] == '1':
		flag = flag or check(s[:-1], dep + 1)
	if s[-2:] == '14':
		flag = flag or check(s[:-2], dep + 1)
	if s[-3:] == '144':
		flag = flag or check(s[:-3], dep + 1)
	return flag


s = input()
if check(s, 0):
	print('YES')
else:
	print('NO')
