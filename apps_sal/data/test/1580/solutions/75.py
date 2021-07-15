import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	is_open=[-1]*n
	graph = [[] for _ in range(n)]
	for _ in range(m):
		x, y, _ = tin()
		graph[x-1].append(y-1)
		graph[y-1].append(x-1)
		
	ret = 0
	for i in range(n):
		if is_open[i] > 0:
			continue
		ret += 1
		q=collections.deque()
		q.append(i)
		is_open[i] = 1
		while q:
			pos = q.pop()
			for t in graph[pos]:
				if is_open[t] > 0:
					continue
				is_open[t] = 1
				q.append(t)
	return ret
		
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

def __starting_point():
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)
__starting_point()
