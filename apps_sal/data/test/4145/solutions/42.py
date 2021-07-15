x = int(input())
while True:
  flg = True
  for i in range(2,x):
    if x % i == 0:
      flg = False
      break
  if flg == True: break
  x += 1
print(x)
