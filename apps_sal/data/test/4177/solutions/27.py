import re
s = input()
answer = re.sub('[a-z]', 'x', s)
print(answer)
