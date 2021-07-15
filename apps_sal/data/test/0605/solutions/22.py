nt=list(map(int,input().split()))
m=max(3*(nt[0])//10,nt[0]-(nt[0]//250)*nt[2])
v=max(3*(nt[1])//10,nt[1]-(nt[1]//250)*nt[3])
if(v>m):
      print('Vasya')
if(v<m):
      print('Misha')
if(v==m):
      print('Tie')

