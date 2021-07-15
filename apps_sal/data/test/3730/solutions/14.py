# http://codeforces.com/contest/446/problem/A

from sys import stdin
inFile = stdin
tokens = []
tokens_next = 0

def next_str():
    nonlocal tokens, tokens_next
    while tokens_next >= len(tokens):
        tokens = inFile.readline().split()
        tokens_next = 0
    tokens_next += 1
    return tokens[tokens_next - 1]

def nextInt():
    return int(next_str())

def nextIncreasingSeg(a, ind):
	if ind >= len(a):
		return None
	r = ind
	while r + 1 < len(a) and a[r + 1] > a[r]:
		r += 1
	return (ind, r)

def myLen(s):
	return s[1] - s[0] + 1

def getBest(a, s0, s1):
	if not s1:
		return myLen(s0)

	if s0[1] - 1 >= s0[0]:
		if a[s0[1] - 1] < a[s1[0]] - 1:
			return myLen(s0) + myLen(s1)
	
	if s1[0] + 1 <= s1[1]:
		if a[s1[0] + 1] > a[s0[1]] + 1:
			return myLen(s0) + myLen(s1)
	return 1 + max(myLen(s0), myLen(s1))

n = nextInt()
a = [nextInt() for i in range(n)]

s0 = nextIncreasingSeg(a, 0)
s1 = nextIncreasingSeg(a, s0[1] + 1)
res = getBest(a, s0, s1)

while s1 and s1[1] + 1 < len(a):
	s0, s1 = s1, nextIncreasingSeg(a, s1[1] + 1)
	res = max(res, getBest(a, s0, s1))

print(res)

