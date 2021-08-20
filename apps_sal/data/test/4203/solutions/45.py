import re
s = input()
print('AC' if re.match('^A[a-z][a-z]*C[a-z]*[a-z]$', s) else 'WA')
