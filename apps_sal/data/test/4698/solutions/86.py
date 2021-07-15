n = int(input())

t = list(map(int,input().split()))

m = int(input())

for i in range(m):
	p,x = list(map(int,input().split()))
	tmpt = t[p-1] 
	t[p-1] = x
	print((sum(t)))
	t[p-1] = tmpt
	

