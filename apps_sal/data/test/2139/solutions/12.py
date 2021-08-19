import re
s = input()
l = len(s)
total = 0
prev = -1
for m in re.finditer('bear', s):
    total += (m.start() - prev) * (l - (m.start() + 3))
    prev = m.start()
print(total)
