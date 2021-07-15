def fact(n):
	ft=1
	while n>0:
		ft=ft*n
		n=n-1
	return ft
n=int(input())
q=2*fact(n)//(n*n)
print(q)

