n = int(input())
ind3 = [0] + [3**i for i in range(1,38)]
ind5 = [0] + [5**i for i in range(1,38)]
flag = False

for a in range(1,38):
  for b in range(1,38):
    if ind3[a] + ind5[b] == n:
      print(a,b)
      flag = True
      break
      
if not flag:
  print(-1)
