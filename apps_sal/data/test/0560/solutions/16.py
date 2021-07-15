s = input().split()
r = int( s[0] )
c = int( s[1] )
a = []
for i in range( r ):
	a.append( input() )
row = r
col = c
for s in a:
	for x in s:
		if x == 'S':
			row -= 1
			break
for i in range( c ):
	for j in range( r ):
		if a[j][i] == 'S':
			col -= 1
			break
			
print( row*c + col*r - col*row )
		

