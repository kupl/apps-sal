n=int(input())
mod=1
for _ in range(n):
	a=int(input())
	if(a%2)==0:
		print(a//2)
	else:
		print(a//2 + mod)
		mod=1-mod


