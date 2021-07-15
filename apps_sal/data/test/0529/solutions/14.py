s=input()
n=int(input())
s=s.lower()
ans=""
for i in range(len(s)):
    x=s[i]
    if(ord(x)<n+97):
        ans+=x.upper()
    else:
        ans+=x.lower()
print(ans)

