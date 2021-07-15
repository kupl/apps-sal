x,y=map(int,input().split())
data=[1,3,1,2,1,2,1,1,2,1,2,1]
if data[x-1]==data[y-1]:
    print('Yes')
else:
    print('No')
