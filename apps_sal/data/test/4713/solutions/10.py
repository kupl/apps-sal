n = int(input())
s = list(input())

x = 0
mx = 0

for a in s:
  if a == "I":
    x +=1
  else:
    x -=1
  if x > mx:
    mx = x
    
print(mx)

