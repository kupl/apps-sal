n,m,q=list(map(int,input().split()))
lr=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
  l,r=list(map(int,input().split()))
  lr[l][r]=lr[l][r]+1

#二次元累積和を作る（横）
for i in range(1,n+1):
  for j in range(1,n+1):
    lr[i][j]=lr[i][j-1]+lr[i][j]

#二次元累積和を作る（縦）
for i in range(1,n+1):
  for j in range(1,n+1):
    lr[i][j]=lr[i][j]+lr[i-1][j]
#答えを出力
for i in range(q):
  p,q=list(map(int,input().split()))
  print((lr[q][q]-lr[p-1][q]-lr[q][p-1]+lr[p-1][p-1]))
  


    
    
  

