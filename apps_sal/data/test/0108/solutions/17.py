s=input()
alpha="abcdefghijklmnopqrstuvwxyz"
c=0
cnt=0
ans=""
while cnt<len(s) and c<26:
    if (ord(s[cnt])-ord('a'))<=c:
        ans+=alpha[c]
        c+=1
    else:
        ans+=s[cnt]
    cnt+=1
if c==26:
    ans+=s[cnt:]
    print(ans)
else:
    print(-1)

