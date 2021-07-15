def empty(d):
	t = '+- -+'
	res = [t]
	for i in range(2 * d - 1): res.append('|   |')
	res.append('+- -+')
	return res

def cover(l):
	numspaces = len(l[0]) - 2
	spaces = numspaces * ' '
	tb = '+-' + spaces + '-+'
	res = [tb]
	for s in l:
		ns = '|' + s + '|'
		res.append(ns)
	res.append(tb)
	return res

def do(s, d):
	blocks = list()
	start = 0
	balance = 0
	for right in range(len(s)):
		if s[right] == '[':
			balance += 1
		else: 
			balance -= 1
		if balance == 0:
			if start + 1 == right:
				blocks.append(empty(d))
			else:
				inner = do(s[start + 1 : right], d - 1)
				covered = cover(inner)
				blocks.append(covered)
			start = right + 1
	res = ["" for _ in range(2 * d + 1)]
	for block in blocks:
		for i in range(len(block)):
			res[i] += block[i]
	return res

def depth(s):
	res = 0
	cur = 0
	for c in s:
		if c == '[':
			cur += 1
		else:
			cur -= 1
		res = max(res, cur)
	return res

n = int(input())
s = input()
for l in do(s, depth(s)):
	print(l)
