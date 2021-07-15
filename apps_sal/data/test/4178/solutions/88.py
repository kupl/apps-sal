n = int(input())
high = list(map(int,input().split()))

a = True

for x in reversed(range(1,n)):
  if high[x-1] >= high[x] + 2:
    a = False
    break
  elif high[x-1] == high[x] + 1:
    high[x-1] = high[x]
    
if a:
  print("Yes")
else:
  print("No")
