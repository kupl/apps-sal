n,d=list(map(int,input().split()))
songs=list(map(int,input().split()))
sparetime=d-(n-1)*10-sum(songs)
if(sparetime<0):
    print(-1)
else:
    print((n-1)*2+sparetime//5)

