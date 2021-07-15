try:
    c=0
    n=int(input())
    for i in range(1,n+1):
        cu=0
        for j in range(1,i+1):
            if i%j==0:
                cu+=1
        if cu==2:
            c+=1
    print(c)
except:
    pass
