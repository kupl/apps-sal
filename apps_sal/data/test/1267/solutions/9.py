
n=int(input())
l=[int(i) for i in input().split()]
s=set(l)
k=len(s)
if 0 in s:
	print (k-1)
else:
	print (k)
