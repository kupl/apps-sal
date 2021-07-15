s=list(map(str,input()))

ans=753-111 #最大値
for i in range(len(s)-2):
	total=s[i]+s[i+1]+s[i+2]
	new=abs(753-int(total))
	ans=min(ans,new)
	

print(ans)
