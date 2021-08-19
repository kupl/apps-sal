import re
n = int(input())
S = input().strip()
s = re.split('[A-Z]+', S)
m = 0
for ss in s:
    x = set(ss)
    m = max(m, len(x))
print(m)
