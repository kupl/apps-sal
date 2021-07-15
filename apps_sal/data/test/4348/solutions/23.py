n,k=list(map(int,input().split()))
a=str(input())
if n!=k:
    b=[]

    for i in range(n):
        b.append([ord(a[i]),i])

    b.sort()

    b=b[k:].copy()

    #print(b)
    a=['']*n
    for i in b:
        a[i[1]]=chr(i[0])




    fini=''.join(a)
    print(fini)
else:
    print()

