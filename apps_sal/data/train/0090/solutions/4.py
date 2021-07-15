for _ in range (int(input())):
    n = int(input())
    a =  [int(i) for i in input().split()]
    l =  [int(i) for i in input().split()]
    b = []
    for i in range (n):
        if l[i]==0:
            b.append(a[i])
    b.sort(reverse=True)
    ind = 0
    for i in range (n):
        if l[i]==0:
            a[i]=b[ind]
            ind+=1
    print(*a)
