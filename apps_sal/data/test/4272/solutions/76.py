import re
n = int(input())
text = input()
pattern = 'ABC'
result = re.findall(pattern, text)
print(len(result))
