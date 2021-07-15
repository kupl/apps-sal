N, A, B = map(int, input().split())
if A+B>N+1: print(-1);return
res,tmp=[],[]
k,l,cnt,sign,m1,m2 = N+1,0,0,1,0,0
while k!=l+1:
    if m1>=A or m2>=B:print(-1);return
    if sign==1:
        if cnt<A-m1:
            k-=1
            tmp.append(k)
            cnt+=1
        else:
            res.extend(reversed(tmp))
            tmp=[]
            cnt=0
            sign=0
            m2+=1
    else:
        if cnt<B-m2:
            l+=1
            tmp.append(l)
            cnt+=1
        else:
            res.extend(reversed(tmp))
            tmp=[]
            cnt=0
            sign=1
            m1+=1
res.extend(reversed(tmp))
print(*res)
