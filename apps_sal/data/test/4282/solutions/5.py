n = int( input() )
m = [[0 for i in range(2)] for j in range(n)]
for k in range(n):
	m[k][0],m[k][1] = map(lambda x: int(x)-1,input().split())
l=list()
l.append(0)
if(m[0][0] in m[m[0][1]]):
	l.append(m[0][1])
	l.append(m[0][0])
else:
	l.append(m[0][0])
	l.append(m[0][1])
cpt = 2
while( l[-1] != l[0]):
	if( m[l[-2]][0] == l[-1] ):
		l.append(m[l[-2]][1])
	else:
		l.append(m[l[-2]][0])
print(" ".join(map(lambda x : str(x+1),l[:len(l)-1])))
