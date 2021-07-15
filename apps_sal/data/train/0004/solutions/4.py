def f(L):
    n=len(L)
    M=[0]*(len(L)+1)
    for i in range(len(L)):
        M[L[i]]=i
    s=[0]*len(L)
    s[0]=1
    sumof=M[1]
    mx=M[1]
    mi=M[1]
    for i in range(2,n):
        k=M[i]
        if k>mx:mx=k
        if k<mi:mi=k
        sumof+=k
        if sumof==(mx*(mx+1))//2-((mi-1)*mi)//2:
            s[i-1]=1
    s[n-1]=1
    return s
for i in ' '*int(input()):
    n=int(input())
    s=f(list(map(int,input().split())))
    for i in s:print(i,end='')
    print()
