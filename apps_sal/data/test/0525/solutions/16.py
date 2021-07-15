for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        if(i!=a[0]):
            c+=1
            break
    if(c!=0):
        print(1)
    else:
        print(n)
