ans=0
op=1
now=0
s=input()
l=len(s)
for i in range(l):
    if s[i]=='+':
        ans=ans+op*now
        now=0
        op=1
    elif s[i]=='-':
        ans=ans+op*now
        now=0
        op=-1
    now=now*10+ord(s[i])-48
ans=ans+op*now
print(ans)
