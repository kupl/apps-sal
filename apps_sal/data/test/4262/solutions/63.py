import sys
from itertools import permutations
N = int(input())
target_list = []
for i in range(2):
  target_list.append(tuple(map(int,input().split())))
  
list=[_ + 1 for _ in range(N)]
per=permutations(list,N)

ans = 0
counter = 1
if target_list[0] == target_list[1]:
  print("0")
  return
for i in per:
  if i in target_list:
    #print(counter)
    if ans == 0:
      ans -= counter
    else:
      ans += counter
    
  counter += 1
print(ans)
    

