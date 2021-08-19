import re
n = int(input())
s = input()
res = re.findall('ABC', s)
print(len(res))
