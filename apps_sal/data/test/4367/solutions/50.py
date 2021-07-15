N = list(map(int,input().split()))
if(N[0] < 10):
  print(N[1]+(100*(10-N[0])))
else:
  print(N[1])
