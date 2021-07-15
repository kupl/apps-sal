import math, sys, itertools

alpha = list('abcdefghijklmnopqrstuvwxyz')
digit = list('1234567890')
spec = ['*', '&', '#']

def find(s):
	dpos = 10000
	apos = 10000
	spos = 10000
	m = len(s)
	for i in range(len(s)):
		if s[i] in alpha:
			if apos>min(m-i,i):
				apos = min(m-i,i)
		if s[i] in digit:
			if dpos>min(m-i,i):
				dpos = min(m-i,i)
		if s[i] in spec:
			if spos>min(m-i,i):
				spos = min(m-i,i)
	return apos, dpos, spos
		

def main():
	n,m = list(map(int, input().split()))
	st = []
	for i in range(n):
		st.append(input())
	
	al = []
	dig = []
	spec = []
	for i in range(n):
		a, d, s = (find(st[i]))
		al.append(a)
		dig.append(d)
		spec.append(s)
		
	sumn = 10000
	for a in range(n):
		for d in range(n):
			for s in range(n):
				if a!=d!=s:
					if sumn>al[a]+dig[d]+spec[s]:
						sumn = al[a]+dig[d]+spec[s]
	print(sumn)

def __starting_point():
	main()

__starting_point()
