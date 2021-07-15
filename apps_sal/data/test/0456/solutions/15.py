import re

n = int(input())
s = input()

result = re.sub(r'ogo(go)*', '***', s)
print(result)

