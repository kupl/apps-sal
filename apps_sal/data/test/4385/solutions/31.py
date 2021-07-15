a = [int(input()) for x in range(5)]
k = int(input())

flg = False

for i, x in enumerate(a):
  for j, y in enumerate(a):
    if i == j:
      continue
      
    flg = flg or abs(y-x) > k
    
print(':(' if flg else "Yay!")
