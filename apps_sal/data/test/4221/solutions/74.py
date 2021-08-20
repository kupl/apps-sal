import re
s = input()
if re.search('s$', s):
    print(s + 'es')
else:
    print(s + 's')
