import sys

def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def rinput():   return map(int, sys.stdin.readline().strip().split()) 
def get_list(): return list(map(int, sys.stdin.readline().strip().split())) 
mod = int(1e9)+7


for _ in range(iinput()):
	n = iinput()
	a = get_list()
	s = set(a)

	if (len(s)==1):
		print(n)
	else:
		print(1)	
