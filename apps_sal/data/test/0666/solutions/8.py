n = int(input())
ans = int((n*2)**0.5)
while ans*(ans+1)//2 > n:
	ans-=1
if ans*(ans+1)//2 == n:
	print(ans)
else:
	print(n-ans*(ans+1)//2)
