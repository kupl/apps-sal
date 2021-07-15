t=int(input())
for you in range(t):
    l=input().split()
    x=int(l[0])
    y=int(l[1])
    n=int(l[2])
    z=(n-y)//x
    print(z*x+y)

