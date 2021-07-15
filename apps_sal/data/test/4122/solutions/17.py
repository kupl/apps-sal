from sys import stdin

H,n=list(map(int,stdin.readline().split()))
arr=list(map(int,stdin.readline().split()))
k=H
d={}
pre=0
cond=False
for i in range(n):
    k+=arr[i]
    pre+=arr[i]
    if pre in d:
        d[pre].append(i+1)
    else:
        d[pre]=[i+1]
    if k<=0:
        ans=i+1
        cond=True
        break
    else:
        pass
if cond==True:
    print(ans)
else:
    s=sum(arr)
    if s<0:
        a=min(list(d.keys()))
        m=(H+a)//abs(s)
        H+=(s*m)
        ans=n*m
        while(H>0):
            l=list([x for x in list(d.keys()) if x+H<=0])
            if len(l)>0:
                case=[]
                for ele in l:
                    case.extend(d[ele])
                ans+=min(case)
                print(ans)
                break
            else:
                H+=s
                ans+=n
    else:
        print(-1)

