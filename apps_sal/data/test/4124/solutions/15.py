# import sys
# sys.stdin=open('F:\\C\\Script\\input.txt','r')
# sys.stdout=open('F:\\C\\Script\\output.txt','w')
# sys.stdout.flush()

I = lambda:[int(i) for i in input().split()]

s = input()
t = input()
n1 = len(s)
n2 = len(t)
if s[-1] != t[-1]:
	print (n1 + n2)
else:
	k = 0
	i = n1 - 1
	j = n2 - 1
	while i >=0 and j >= 0:
		if s[i] != t[j]:
			break
		i -= 1
		j -= 1
	print (i + j + 2)
