import re
n = input()
flag = re.match('[a-z]', n)
print('a') if flag != None else print('A')
