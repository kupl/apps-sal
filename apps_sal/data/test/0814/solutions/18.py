n=int(input())
a=list(map(int,input().split()))
li=[ sum( x>=i for x in a) for i in range(1,101)]
print(*list( sum( x+i>=n for x in li ) for i in range(0,n) ) )

