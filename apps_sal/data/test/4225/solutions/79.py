a,b,c,k=list(map(int,input().split()))

if k<=a:
    ans=k
elif a<k<=b:
    ans=a
else :
    ans=a-(k-a-b)
print(ans)

