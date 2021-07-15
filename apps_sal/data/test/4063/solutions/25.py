n = int(input())
dif = list(map(int,input().split()))
new_dif = list(sorted(dif))
if new_dif[n//2-1] == new_dif[n//2]:
  print(0)
  
else:
  print(new_dif[n//2]-new_dif[n//2-1])
