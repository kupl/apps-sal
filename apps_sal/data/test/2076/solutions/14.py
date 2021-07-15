t=int(input())
for i in range(t):
    g=[int(x) for x in input().split()]
    h=min(g[1],int(g[2]/2))
    j=min(g[0],int((g[1]-h)/2))
    print(3*(h+j))

