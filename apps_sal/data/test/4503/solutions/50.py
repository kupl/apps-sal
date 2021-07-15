health, num = map(int, input().split())
num_list = [num for num in list(map(int, input().split()))]
for _ in num_list:
  health -= _
  
if health > 0:
  print("No")
else:
  print("Yes")
