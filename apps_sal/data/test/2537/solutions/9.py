def subseq(a,b):
    n=len(a)
    m=len(b)
    i=0 
    j=0 
    c=0 
    while i<n and j<m :
        if a[i]==b[j]:
            i+=1 
            j+=1 
            c+=1 
        else:
            j+=1 
    return c==n 
for _ in range(int(input())):
    s=input()
    t=input() 
    p=input()
    from collections import Counter 
    c1=Counter(s)
    c2=Counter(t)
    c3=Counter(p)
    f=1 
    if not subseq(s,t):
        f=0 
    l=[chr(i) for i in range(97,123)]
    for x in l:
        if c1[x]>c2[x]:
            f=0 
            break  
        req=c2[x]-c1[x]
        if c3[x]<req:
            f=0 
            break 
    print('YES' if f else 'NO')
