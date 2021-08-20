import re
n = int(input())
s = input()
ans = 0
ss = re.split('[A-Z]+', s)
print(max(list(map(len, list(map(set, ss))))))
'\n11\naaaaBAAAVDAaabAbA\n'
