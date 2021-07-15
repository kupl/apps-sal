t=int(input())
for i in range(t):
    n,x,a,b=[int(x) for x in input().split(' ')]
    print(min(n-1,abs(a-b)+x))

