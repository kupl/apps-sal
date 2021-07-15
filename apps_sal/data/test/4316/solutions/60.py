s=input()
d={}
for i in range(4):
    if s[i] not in d:
        d[s[i]]=1
    else:
        d[s[i]]+=1
ans="Yes"
for i in d:
    if d[i]!=2:
        ans="No"
print(ans)
