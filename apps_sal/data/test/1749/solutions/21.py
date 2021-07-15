'''input
5 2 4
3 4 2 3 1
3 2 3 4 1
'''
n, l, r = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))
if a[:l-1] == b[:l-1] and a[r:] == b[r:] and sorted(a[l-1:r]) == sorted(b[l-1:r]):
	print("TRUTH")
else:
	print("LIE")
