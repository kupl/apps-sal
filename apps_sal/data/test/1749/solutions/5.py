lmap = lambda f, x: list(map(f, x))
n,l,r = lmap(int, input().split())
l-=1 
a = lmap(int, input().split())
b = lmap(int, input().split())

a1 = a[l:r]
a2 = b[l:r]
good = (sorted(a1)==sorted(a2)) and (a[:l] == b[:l]) and (a[r:] == b[r:])
if good:
	print('TRUTH')
else:
	print("LIE")
