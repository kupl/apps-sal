N = int(input())
n = 0
blue = []
while n<N:
  blue.append(input())
  n += 1

M = int(input())
m = 0
red = []
while m<M:
  red.append(input())
  m += 1
  
set_blue = set(blue)  
scores = []
for s in set_blue:
  score = blue.count(s) - red.count(s)
  scores.append(score)
  
ms = max(scores)
if ms>=0:
  print(ms)
else:
  print(0)
