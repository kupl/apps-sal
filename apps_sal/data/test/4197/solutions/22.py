N = int(input())
L = list(map(int,input().split()))
d = {}
for i in range(N):
  d[L[i]] = i + 1
for j in range(1 , N + 1):
  print(d[j] , end = ' ')
  
  

