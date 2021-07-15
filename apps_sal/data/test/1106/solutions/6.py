#!python3
n = int(input())
a = input().split()
a = [int(i) for i in a]

def solve(n, a, added):
	last = a[-2**n:]
	new = []

	for i in range(0, 2**n-1, 2):
		#print(last[i])
		x = last[i]
		y = last[i+1]
		new.append(max(x,y))
		added = added + abs(x-y)

	a = a[:-2**n]

	if a==[]:
		a = [0]

	for i in range(1, 2**(n-1)+1):
		a[-i] = a[-i] + new[-i]

	n = n-1
	if n==0:
		print(added)
	else:
		solve(n, a, added)

solve(n, a, 0)
