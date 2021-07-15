def go():
    n,k = map(int,input().split())
    x=1
    for i in range(n-2,-1,-1):
        if k>n-1-i:
            k-=n-1-i
        else:
            ans=['a']*n
            ans[i]='b'
            ans[n-k]='b'
            return ''.join(ans)




# x,s = map(int,input().split())
t = int(input())
# t=1
ans=[]
for _ in range(t):
    # go()
    ans.append(str(go()))

print('\n'.join(ans))
