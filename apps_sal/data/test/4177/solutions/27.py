import re
s = input()
answer = re.sub(r'[a-z]', 'x', s)
print(answer)
