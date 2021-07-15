#!/usr/bin/env python3

n = int(input().strip())
s = input().strip()

def solve(n, s):
	if '11' in s:
		return False
	if '000' in s:
		return False
	if s.endswith('00') or s.startswith('00'):
		return False
	if s == '0':
		return False
	return True
	
if solve(n, s):
	print ('Yes')
else:
	print ('No')

