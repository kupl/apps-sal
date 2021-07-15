import sys 
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

for t in range(int(input())):
  n, a, b = list(map(int, input().split()))
  s = input()
  arr = [['0', 1]]
  for i in range(1, n):
    if s[i] == arr[-1][0]:
      arr[-1][1] += 1
    else:
      arr.append([s[i], 1])
  
  if len(arr) == 1:
    pipe = n
    pillar = n + 1
  else:
    pipe = n + 2
    pillar = arr[0][1] + arr[-1][1] + 2 * (n + 1 - arr[0][1] - arr[-1][1])
    for i, j in arr[1:-1]:
      if i == '0' and j >= 2 and (j-1)*b > 2*a:
        pipe += 2
        pillar -= j-1
        
  print(pipe*a + pillar*b)



      

      
        


