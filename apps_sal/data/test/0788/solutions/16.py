def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
x = input()
ret = 1
for s in x:
	if(is_number(s)):
		if(s == '0'):
			ret = ret + 9
		else:
			ret = ret + int(s)

print(ret)
