

ans=[]
def func(f,b):
    nonlocal ans
    dic={}
    k=0
    for i in range(len(f)):
        dic[f[i]]=-1
    for i in range(len(f)):
        if dic[f[i]]!=-1:
            dic[f[i]]=-10
        else:
            dic[f[i]]=i+1
    for i in b:
        if i in dic:
            if dic[i]==-10:
                k=1
            ans.append(dic[i])
        else:
            return 3
    if k:
        return 2
    return 1


q=list(map(int,input().split()))
n,m=q[0],q[1]
f=list(map(int,input().split()))
b=list(map(int,input().split()))
p=func(f,b)
if p==1:
    print("Possible")
    for i in ans:
        print(i,end=' ')
elif p==2:
    print("Ambiguity")
else:
    print("Impossible")
