import re
n = int(input())
s = input()
print(re.sub('ogo(go)*', '***', s))
