S,Q=input(),int(input())
l,r='',''
reverse=0
for i in range(Q):
    T=input().split()
    if T[0]=='1':reverse=0 if reverse else 1
    else:
        if T[1]=='1':
            if reverse:r=r+T[2]
            else:l=T[2]+l
        else:
            if reverse:l=T[2]+l
            else:r=r+T[2]
if reverse:
    s=list(l+S+r);s.reverse()
    print(''.join(s))
else:
    print(l+S+r)
