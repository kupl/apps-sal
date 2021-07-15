name=input()
char_set=set()
for char in name :
	char_set.add(char)
if len(char_set) % 2 :
	print('IGNORE HIM!')
else :
	print('CHAT WITH HER!')

