n=int(input())
for i in range(n):
    x,y=list(map(int,input().split()))
    stolb=[0]*y
    stroki=[0]*x
    al=[]
    for j in range(x):
        st=input()
        al.append(st)
        for j2 in range(y):
            if st[j2]=='.':
                stroki[j]+=1
                stolb[j2]+=1
    mi=1000000000000000
    for j in range(x):
        for j2 in range(y):
            if al[j][j2]=='.':
                if stroki[j]+stolb[j2]-1<mi:
                    mi=stroki[j]+stolb[j2]-1
            else:
                if stroki[j]+stolb[j2]<mi:
                    mi=stroki[j]+stolb[j2]
    print(mi)

