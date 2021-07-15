n=int(input())
x=list(map(int,input().split()))
xm=max(x)
def ra(a): #圧縮された要素を非保持
    ll,l=[0]*xm,1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            l+=1
        else:
            ll[a[i]]+=l
            l=1
    ll.append(l)
    return ll
b=ra(sorted(x))
d=0
for i in b:
    d+=(i*(i-1))//2
for i in range(n):
    print(d-b[x[i]]+1)
