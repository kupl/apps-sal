t=int(input())
for you in range(t):
    n=int(input())
    print(2)
    l=[i+1 for i in range(n)]
    for i in range(n-1):
        print(l[-1],l[-2])
        z=(l[-1]+l[-2]+1)//2
        l.pop(-1)
        l.pop(-1)
        l.append(z)

