t=int(input())
while t:
    t-=1
    a,b,c=list(map(int,input().split()))
    print(max(a+b,b+c,c+a))

