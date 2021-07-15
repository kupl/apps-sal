n = input()
count = 0

for i in range(int(n)):
  roll = input()

  if roll[0] == roll[2]:
    count = count +1
    if count == 3:
      break
  else:
    count = 0
    
    
if count >= 3:
  print("Yes")
else:
  print("No")

