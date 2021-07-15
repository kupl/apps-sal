s = int(input())

if s < 3:
  print(4)
  return

cnt = 1
val = s
while True:
  if cnt > 1 and val == 1:
    break
  
  if val % 2 == 0:
    val = val//2
  else:
    val = val*3+1
    
  cnt += 1
             
print(cnt+1)
