import sys

m, n = map(int, sys.stdin.readline().split())

latestStartTime = [0 for i in range(n)]

for i in range(m):
  picture = [int(s) for s in sys.stdin.readline().split()]

  for j in range(n): 
    if j > 0 and latestStartTime[j-1] > latestStartTime[j]:
      latestStartTime[j] = latestStartTime[j-1]
    latestStartTime[j] += picture[j]
  if i > 0:
    print(" ", end="")
  print(latestStartTime[n-1], end="")
print()
  
  
