n,m = map(int , input().split())
i = 0
while(i//2 <n or i//3 < m or i//2 + i//3 - i//6 < n+m):
	i+=1
print(i)
