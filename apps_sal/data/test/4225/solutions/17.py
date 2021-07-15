A,B,C,K = map(int,input().split())

if K >= A+B :
  print(A-(K-A-B))
elif K >= A:
  print(A)
else:
  print(K)
