import sys, math

line = input()
length = len(line)
cur = 'a'
sumn = 0
for c in line:
	diff = abs(ord(c)-ord(cur))
	sumn += min(diff, 26 - diff)
	cur = c
print(sumn)

