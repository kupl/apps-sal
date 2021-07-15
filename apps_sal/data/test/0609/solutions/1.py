#!/usr/bin/env python3

def read_ints():
	return list(map(int, input().strip().split()))

n, = read_ints()

t = [ input() for _ in range(n) ]

def check():
	if t[0][0] == t[0][1]:
		return False
	
	for x in range(n):
		if t[x][x]!=t[0][0]:
			return False
		if t[x][n-x-1]!=t[0][0]:
			return False

		for y in range(n):
			if x==y or x==n-y-1:
				continue
			if t[x][y] != t[0][1]:
				return False
	return True

print("YES" if check() else "NO")





