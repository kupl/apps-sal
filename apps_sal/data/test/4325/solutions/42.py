n,x,t = map(int,input().split())

ans = t*(n//x + 1)
if(n %  x == 0):
	ans -= t
print(ans)
