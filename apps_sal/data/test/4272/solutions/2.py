import re
n = int(input())
s = input()
res = re.findall(r'ABC',s)
print(len(res))
