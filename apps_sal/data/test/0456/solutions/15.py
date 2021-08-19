import re
n = int(input())
s = input()
result = re.sub('ogo(go)*', '***', s)
print(result)
