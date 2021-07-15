N=int(input())
A=[int(x) for x in input().split()]
numdict=dict()
for h in range(N):
    if A[h] in numdict.keys():
        numdict[A[h]]+=1
    else:
        numdict[A[h]]=1
all_select_two=0
for i in numdict.keys():
    value=numdict[i]
    all_select_two+=value*(value-1)//2
ans=0
for k in range(N):
    j=A[k]
    value=numdict[j]
    ans=all_select_two-value+1
    print(ans)
