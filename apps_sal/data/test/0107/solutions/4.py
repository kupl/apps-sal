s = input()
if(s.count('1') > 0):
	i = s.index('1')
	s = s[i:]
	if(s.count('0') >= 6):
		print('yes')
	else:
		print('no')
else:
	print('no')
