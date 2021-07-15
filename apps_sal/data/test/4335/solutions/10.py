n=int(input())
s=input()
s1=n//2
ans="No"
if n&1!=1:
    if s[:s1]==s[s1:]:
        ans="Yes"
print(ans)
