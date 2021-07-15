n=int(input())
xy=[list(map(int, input().split())) for i in range(n)]
z=list(map(lambda x: x[0]+x[1], xy))
w=list(map(lambda x: x[0]-x[1], xy))
print(max(max(z)-min(z), max(w)-min(w)))
