def f():
    n=int(input())
    a=[0]*5
    b=[0]*5

    X = [int(x) for x in input().split()]
    for x in X:
        a[x-1]+=1

    X = [int(x) for x in input().split()]
    for x in X:
        b[x-1]+=1

    for i in range(5):
        if (a[i]+b[i])%2==1:
            print('-1')
            return

    x=0
    for i in range(5):
        x += abs(a[i]-b[i])/2

    print(int(x/2))

f()

