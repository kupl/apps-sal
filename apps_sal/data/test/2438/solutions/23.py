n=int(input())
a=list(input())
ans=n*(n-1)//2
l=1
for itr in range(1,n):
    #print(ans)
    if a[itr]==a[itr-1]: l+=1
    else: 
        ans-=l
        l=1
l=1
a=a[::-1]
for itr in range(1,n):
    if a[itr]==a[itr-1]: l+=1
    else: 
        ans-=l-1
        l=1
print(ans)
