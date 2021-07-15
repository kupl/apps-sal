n=int(input())
for ccc in range(n):
    c,s=list(map(int,input().split()))
    x=s//c
    y=s-x*c
    print(y*(x+1)**2+(c-y)*x**2)

