n=int(input())
s=[100]*26
for i in range(n):
    a=[0]*26
    for j in list(input()):
        a[ord(j)-97]+=1
    for j in range(26):
        s[j]=min(s[j],a[j])
ans=''
for i in range(26):
    for j in range(s[i]):
        ans=ans+chr(i+97)
print(ans)
