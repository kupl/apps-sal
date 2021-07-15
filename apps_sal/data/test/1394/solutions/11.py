s = input()
wyn = 0
for i in s:
	if i == "a":
		wyn += 1
l = len(s)
import sys
if (l-wyn) % 2 != 0:
	print(":(")
	return
dl = (l - wyn) // 2 
pocz = s[:l-dl]
kon = s[l-dl:]
b = []
c= []
for i in pocz:
	if i != "a":
		b.append(i)
for i in kon:
	c.append(i)
if b == c:
	print(pocz)
else:
	print(":(")
