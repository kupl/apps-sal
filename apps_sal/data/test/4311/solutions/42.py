s=int(input())
a=[]
na=[]
a.append(s)
for i in range(1,10**6):
    if a[i-1]%2==0:
        a.append(a[i-1]/2)
    else:
        a.append(a[i-1]*3+1)
    na=set(a)
    if len(na)!=i+1:
        print(i+1)
        return
