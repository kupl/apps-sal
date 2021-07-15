import os, sys, re, math, queue

S = input()

al = 'abcdefghijklmnopqrstuvwxyz'

def doit():
	for a in al:
		m = re.search(a+'{2,}', S)
		if m:
			return str(m.start()+1) + ' ' + str(m.end())
		m = re.search(a+'[^'+a+']'+a, S)
		if m:
			return str(m.start()+1) + ' ' + str(m.end())
	
	return '-1 -1'

print(doit())
