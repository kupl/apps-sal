s=list(input())
ans=0
n=len(s)
for i in range(n-1):
    if s[i]=='V' and s[i+1]=='K': ans+=1
for t in range(len(s)):
    anst=0
    ss=s[:]
    if ss[t]=='V': ss[t]='K'
    else: ss[t]='V'
    for i in range(n-1):
        if ss[i]=='V' and ss[i+1]=='K': anst+=1
    if anst>ans: ans=anst
print(ans)
