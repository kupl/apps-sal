

import sys

line = input().split()
n = int(line[0])
s = int(line[1])
t = int(line[2])

line = input().split()
p = []
for i in line:
	p.append(int(i))

if s == t:
	print(0)
	return

pos = s
moves = 0
while pos != t:
	pos = p[pos - 1]
	moves = moves + 1
	if pos == t:
		print (moves)
		return
	if pos == s:
		print(-1)
		return

