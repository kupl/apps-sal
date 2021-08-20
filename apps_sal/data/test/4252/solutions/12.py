import re
N = int(input())
print(sum((len(g) - 2 for g in re.findall('xxx+', input()) if len(g) >= 3)))
