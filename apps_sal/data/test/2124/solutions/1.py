#!/usr/bin/env python3

import re

def cont(line, user):
	return re.search('[^a-zA-Z0-9]' + user + '[^a-zA-Z0-9]', '_' + line + '_')

tests = int(input())
for test in range(tests):
	input()
	users = input().rstrip('\n').split(' ')
	linecnt = int(input())
	lines = [input().rstrip('\n') for _ in range(linecnt)]
	lines = [x.split(':', maxsplit=1) for x in lines]
	poss = [[]] * linecnt
	for i, (user, line) in enumerate(lines):
		if user != '?':
			poss[i] = [user]
		else:
			poss[i] = [u for u in users if not cont(line, u)]

	el = list(enumerate(lines))
	rel = list(reversed(el))

	changed = False
	while True:
		for i, (user, line) in el:
			if i > 0 and len(poss[i-1]) == 1:
				if poss[i-1][0] in poss[i]:
					poss[i].remove(poss[i-1][0])
					changed = True
		for i, (user, line) in rel:
			if i < linecnt - 1 and len(poss[i+1]) == 1:
				if poss[i+1][0] in poss[i]:
					poss[i].remove(poss[i+1][0])
					changed = True
		if not changed:
			break
		changed = False

	if all(len(p) > 0 for p in poss):
		for i, p, (user, line) in zip(list(range(linecnt)), poss, lines):
			if i > 0:
				if poss[i-1][0] in p:
					p.remove(poss[i-1][0])
			print(p[0] + ':' + line)
	else:
		print('Impossible')

