#!/usr/bin/env python3

import sys

s = sys.stdin.readline().strip()
alph = 'abcdefghijklmnopqrstuvwxyz'

res = []
ia = 0
done = False

for i, c in enumerate(s):
	if c <= alph[ia]:
		res.append(alph[ia])
		ia += 1
		if ia == len(alph):
			done = True
			idone = i
			break
	else:
		res.append(c)

if done:
	print(''.join(res) + s[idone +1:])
else:
	print ('-1')


