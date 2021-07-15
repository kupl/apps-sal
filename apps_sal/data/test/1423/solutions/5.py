n, l, r = map(int,input().split(" "))
a = list(map(int, input().split(" ")))
compressed = list(map(int, input().split(" ")))

#print('n,l,r')
#print(n,l,r)

b = [0]*n 

lastmod = -1
lol = list(zip(compressed, enumerate(a)))
#print('sorted lol')
#print(sorted(lol))

for i, (pos, val)  in sorted(lol): 
#	print('position of a, val of a in that pos')
#	print(pos, val) 
#	print('lastmod')
#	print(lastmod)
	if i == 1:
		b[pos] = l
		lastmod = pos
	if i > 1: 	
		b[pos] = max(b[lastmod] - a[lastmod] + val + 1, l)
		if b[pos] > r: 
			print("-1")
			return
		lastmod = pos
#	print('b is now')
#	print(b)

for i in b: 
	print(i, end=" ")
	 		

