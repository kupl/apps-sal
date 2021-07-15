import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

n = mint()
l = [[] for i in range(27)]
r = [[] for i in range(27)]
s = minp()
for i in range(n):
	if s[i] == '?':
		l[26].append(i)
	else:
		l[ord(s[i])-ord('a')].append(i)
s = minp()
for i in range(n):
	if s[i] == '?':
		r[26].append(i)
	else:
		r[ord(s[i])-ord('a')].append(i)
res = [0]*n
rp = 0
best = 0
for i in range(26):
	for j in range(min(len(l[i]),len(r[i]))):
		res[rp] = (l[i].pop()+1, r[i].pop()+1)
		rp += 1
		best += 1
for i in range(26):
	while len(l[i]) > 0 and len(r[26]) > 0:
		res[rp] = (l[i].pop()+1, r[26].pop()+1)
		rp += 1
		best += 1
for i in range(26):
	while len(r[i]) > 0 and len(l[26]) > 0:
		res[rp] = (l[26].pop()+1, r[i].pop()+1)
		rp += 1
		best += 1
i = 0
j = 0
while i < 27 or j < 27:
	if i < 27 and len(l[i]) == 0:
		i += 1
	elif j < 27 and len(r[j]) == 0:
		j += 1
	else:
		if i == j or i == 26 or j == 26:
			best += 1
			res[rp] = (l[i].pop()+1, r[j].pop()+1)
			rp += 1
		else:
			l[i].pop()+1
			r[j].pop()+1
print(best)
for i in range(rp):
	print(*res[i])

