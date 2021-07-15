n,k,q=map(int, input().split())
if q==1:
    print(0)
    return()
*a,=map(int, input().split())
a+=[-1]
ans=10**10
for i in range(n):
    ai=a[i]
    tmp=[10**11]##15行目でtmp[:0]になるから
    tmp2=[ai]
    for j in range(n+1):
        if i==j:
            continue
        if a[j]<ai:
            tmp.sort()
            if len(tmp)>=k+1:
                tmp2+=tmp[:-k]
            tmp=[10**11]###
        else:
            tmp.append(a[j])
            #print("test",tmp)
    tmp2.sort()
#    print(tmp,tmp2)
    if len(tmp2)>=q:    
#        print("test2")
        ans=min(ans,tmp2[q-1]-ai)
print(ans)
