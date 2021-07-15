import re
st = input()
s = re.split(r'[\s]', st)
x1 = int(s[0])
y1 = int(s[1])
x2 = int(s[2])
y2 = int(s[3])
s = ((y2 - y1) // 2 + 1) * ((x2 - x1) // 2 + 1) + ((y2 - y1) // 2 * (x2 - x1) // 2)
print (s)
