n=int(input())
a=list(map(int,input().split()))
hindo=dict()
for i in a:
    if i in hindo:
        hindo[i]+=1
    else:
        hindo[i]=1
ans=0
for num,cnt in hindo.items():
    if num==cnt:
        continue
    else:
        if num>cnt:
            ans+=cnt
        else:
            ans+=cnt-num
print(ans)
