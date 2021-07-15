N=int(input())

AB=[list(map(int,input().split())) for _ in range(N)]

AB=sorted(AB,key=lambda i:i[1])

count=0
for i in range(N):
  
  count+=AB[i][0]
 
  if AB[i][1] < count:
    print('No')
    return
else:
  print('Yes')
