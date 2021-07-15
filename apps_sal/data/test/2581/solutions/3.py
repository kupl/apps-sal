from sys import stdin
input = stdin.buffer.readline
I = lambda : list(map(int,input().split()))

n,=I()
l=[]
for i in range(n):
	l.append(I())
d={};su={};s=0;an=[1,1,2,1]
for i in range(n):
	for j in range(n):
		d[i-j]=d.get(i-j,0)+l[i][j]
		su[i+j]=su.get(i+j,0)+l[i][j]
x=0;y=0
for i in range(n):
	for j in range(n):
		p=d[i-j]+su[i+j]-l[i][j]
		if (i+j)%2:
			if p>x:
				an[0],an[1]=i+1,j+1
				x=p
		else:
			if p>y:
				an[2],an[3]=i+1,j+1
				y=p
s=x+y
print(s)
print(*an)

