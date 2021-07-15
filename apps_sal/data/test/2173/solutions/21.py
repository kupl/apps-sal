n = int(input())
lis = list(map(int,input().split()))
li = sorted(list(range(len(lis))), key=lambda k: lis[k])
ans=[0]*n
prev=lis[li[0]];ans[li[0]]=lis[li[0]]
for i in range(1,n):
    g=li[i]
    if prev >= lis[g]:
        prev+=1
        ans[g]=prev
    else:
        prev=lis[g]
        ans[g]=lis[g]
print(*ans)

