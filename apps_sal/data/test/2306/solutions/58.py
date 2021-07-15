n=int(input())
inpt=list(map(int,input().split()))
inpv=list(map(int,input().split()))

t=inpt+[0]
v=inpv+[0]

T=sum(t)
M=[0]

nowt=2*t[0]
nowmaxv=v[0]
nowv=M[0]
i=0

for time in range(2*T):
    if nowv+0.5<=v[i]:
        M.append(nowv+0.5)
    else:
        M.append(nowv)
    nowt-=1
    nowv=M[-1]
    if nowt==0:
        i+=1
        nowt=2*t[i]
        nowmaxv=v[i]
        nowv=min(nowv,nowmaxv)
        
t=list(reversed(inpt))+[0]
v=list(reversed(inpv))+[0]
m=[0]

nowt=2*t[0]
nowmaxv=v[0]
nowv=M[0]
i=0

for time in range(2*T):
    if nowv+0.5<=v[i]:
        m.append(nowv+0.5)
    else:
        m.append(nowv)
    nowt-=1
    nowv=m[-1]
    if nowt==0:
        i+=1
        nowt=2*t[i]
        nowmaxv=v[i]
        nowv=min(nowv,nowmaxv)

ans=[min(M[i],m[-i-1]) for i in range(len(M))]
print(sum([min(ans[i],ans[i+1])+(ans[i+1]-ans[i])**2 for i in range(len(ans)-1)])/2)
