sa=int(input())
if sa%2==1:
    print(-1)
else:
    ans=''
    for x in range(1, int(sa/2+1)):
        ans+=str(2* x)
        ans+=' '
        ans+=str(2*x-1)
        ans+=' '
    print(ans.strip())

