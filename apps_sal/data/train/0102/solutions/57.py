n=int(input())
for i in range(n):
    a=int(input())
    t=['1','2','3','4','5','6','7','8','9']
    keks=0
    c=0
    while True:
        if int(t[keks])>a:
            break
        else:
            c+=1
            t[keks]+=t[keks][0]
            keks+=1
        if keks==9:
            keks=0
    print(c)
