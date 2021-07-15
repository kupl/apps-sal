r,g,b = map(int,input().split())
ans = 0 
if 0 in [r,g,b]:
	ans = r//3+g//3+b//3
else: 
	ans  = max(r//3+g//3+b//3+min(r%3,b%3,g%3),1+(r-1)//3+(g-1)//3+(b-1)//3+min((r-1)%3,(g-1)%3,(b-1)%3),2+(r-2)//3+(g-2)//3+(b-2)//3+min((r-2)%3,(g-2)%3,(b-2)%3))
print(ans)
