import re
st = input()
s = re.split(r'[\s]', st)
n = int(s[0])
t = int(s[1])
print (n * 1.000000011 ** t)
