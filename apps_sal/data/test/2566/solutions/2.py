def f(target):
    i,j=0,0
    n=14
    l=n
    c=0
    while j<n:
        if a[j]:
            c+=1

        while c>target or a[i]==0:
            if a[i]:
                c-=1
            i+=1

            if i==j:
                break

        if c==target:
            l = min(l,j-i+1)

        j+=1

    return l

for _ in range(int(input())):
    k=int(input())
    a=[int(i) for i in input().split()]

    t=sum(a)
    ans=k//t * 7
    rem=k%t
    a*=2
    if rem==0:
        print(ans-7 + f(t))

    else:
        print(ans + f(rem))
