def isLucky(t):
	if 7==t%10:
		return True
	if (t//60)%10==7:
		return True
	return False

x = int(input())
h,m = list(map(int,input().split()))
ct = h*60+m
ans = 0
while (not isLucky(ct)):
	ct = (ct-x)%(60*24)
	ans+=1
print(ans)

