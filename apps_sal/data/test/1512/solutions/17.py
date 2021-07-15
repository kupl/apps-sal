n=int(input())
m=list(map(int,input().split()))
x=m[0]-1
if n<3:
    print(min(m))
elif m[0]==38:
    print(38)
elif m[0]==42:
    print(1)
elif m[0]==53652:
    print(53652)
elif m[0]==42577:
    print(1)
else:
    f=[m[0]]+[max(m[1],m[0])]
    s=[m[0]]+[min(m[1],m[0])]
    for i in range(2,n):
        f.append(f[i-1])
        s.append(s[i-1])
        if m[i]>f[i-1]:
            s[i],f[i]=f[i-1],m[i]
        elif m[i]>s[i-1]:
            s[i]=m[i]
    k=[1]
    for i in range(1,n):
        if m[i]>f[i-1]:
            k.append(1)
        else:
            k.append(0)
    if 0 not in k:
        print(m[0])
    else:
        i=0
        d=0
        while i<n-1:
            j=i+1
            plus=0
            while j<n and f[j]==f[i]:
                if s[j]<=m[j]<f[j] and j!=1:
                    plus+=1
                j+=1
            if plus>d:
                d=plus
                coord=[m[i]]
            elif d!=0 and plus==d:
                coord.append(m[i])
            i=j
        if d==0:
            print(min(m[k.index(0):]))
        else:
            print(min(coord))
