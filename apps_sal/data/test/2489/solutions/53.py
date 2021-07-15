n=int(input())
an=[int(i) for i in input().split()]
an.sort()
maxA=an[-1]

ans_table=[0]*(maxA+1)


for ai in an:
    for k in range(1,int(maxA/ai)+1):
        ans_table[ai*k]+=1
ans=0
for ai in an:
    if ans_table[ai]==1:
        ans+=1

print(ans)
