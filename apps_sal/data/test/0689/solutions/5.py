for _ in range (int(input())):
    n=int(input())
    d=dict()
    for i in range (n):
        s=input()
        for j in s:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
    c=1
    for i in d:
        if d[i]%n!=0:
            c=0
            break
    if c==1:
        print("YES")
    else:
        print("NO")
