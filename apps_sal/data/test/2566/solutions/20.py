from sys import stdin
for _ in range(int(stdin.readline())):
    K=int(stdin.readline())
    lst=[*map(int,stdin.readline().split())]
    ans,item=[],0
    for i,x in enumerate(lst):
        if x==1:ans.append(i);item+=1
    res=100000000000000000000000
    for i,x in enumerate(ans):
        k=K
        elem=0
        if k<=item-i:elem=ans[i+k-1]-x+1
        else:
            elem+=(7-x)
            k-=(item-i)
            elem+=((k//item)*7)
            k=k%item
            if k==0:elem-=(7-ans[-1]-1)
            else:elem+=ans[k-1]+1
        res=min(res,elem)
    print(res)
