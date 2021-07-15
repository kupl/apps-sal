n=int(input())
a=input().split('0')
ans=0
for i in a:
	ans=ans*10+len(i)
print(ans)
