s=list(map(str,input()))

lst=[]
for i in range(len(s)-2):
	total=s[i]+s[i+1]+s[i+2]
	ans=abs(753-int(total))
	lst.append(ans)
	

print(min(lst))
