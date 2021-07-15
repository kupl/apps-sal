n = int(input())
s,t = map(str, input().split())
ans = list()
for i in range(n):
	ans.append(s[i])
	ans.append(t[i])
print(*ans,sep="")
