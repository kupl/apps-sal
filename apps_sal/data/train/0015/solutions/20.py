t=int(input())
for i in range(t):
    a,b,x,y=list(map(int,input().split()))
    r = [a*y, b*x, a*(b-y-1), b*(a-x-1)]
    print(max(r))

