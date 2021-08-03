import re
n = int(input())
s = input()
ans = 0
ss = re.split(r'[A-Z]+', s)
print(max(list(map(len, list(map(set, ss))))))

"""
11
aaaaBAAAVDAaabAbA
"""
