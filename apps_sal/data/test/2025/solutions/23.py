q=int(input())
for i in range(q):
    a=int(input())
    k=0
    if a==11:
        print(-1)
        continue
    if a%2==1:
        if a<9:
            print(-1)
            continue
        else:
            a-=9
            k+=1
    k+=a//4
    a%=4
    if k>0:
        print(k)
    else:
        print(-1)
