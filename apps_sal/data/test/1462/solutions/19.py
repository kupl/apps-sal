n,k=list(map(int,input().split()))
s=input()
a=[0]*26
for c in s:
    a[ord(c)-ord('A')]+=1
a.sort(reverse=True)
ans=0
for i in range(26):
    if(k<=a[i]):
        ans+=k**2
        break
    else:
        ans+=a[i]**2
        k-=a[i]
print(ans)

