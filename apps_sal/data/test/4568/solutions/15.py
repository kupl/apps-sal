n=int(input())
s=input()
ans=0
for i in range(n-1):
    a=set()
    b=set()
    for j in range(i):
        a.add(s[j])
    for j in range(i,n):
        b.add(s[j])
    ans=max(ans,len(a&b))
print(ans)
