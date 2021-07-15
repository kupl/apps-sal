__author__ = 'Think'
k2, k3, k5, k6=[int(i) for i in input().split()]
r=min(k5, k6)
if r>k2:
	print(256*k2)
else:
	print(256*r+32*min(k3, k2-r))
