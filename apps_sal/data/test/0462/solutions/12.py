a,b,c = list(map(int, input().split()))
ans = 305
for i in range(1,101):
	ans = min(ans, abs(i-a)+ abs(i-b)+abs(i-c))
print(ans)

